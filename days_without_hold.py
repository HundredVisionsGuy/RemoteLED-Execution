#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime
import os
from datetime import date
from datetime import datetime
from datetime import timedelta
import day_finder
import requests as re
from icalendar import Calendar
from pytz import timezone
from days_until_dates import TARGET_DATES, days_until


def is_weekday(day):
    return day in ("Mon", "Tue", "Wed", "Thu", "Fri")


def get_school_day_from_day_finder() -> str:
    """Get A/B day from the current day-finder calendar."""
    try:
        school_day = day_finder.get_current_day()
        if not school_day:
            return ""

        normalized_day = str(school_day).upper()
        has_a = "A DAY" in normalized_day
        has_b = "B DAY" in normalized_day

        if has_a and not has_b:
            return "A DAY"
        if has_b and not has_a:
            return "B DAY"
    except Exception as ex:
        print(f"Error using day_finder: {ex}")
    return ""


def load_font_with_fallback(font) -> str:
    """Load a font from known paths and return the resolved path used."""
    candidate_paths = [
        "helvR12.bdf",
        "7x13.bdf",
        os.path.join(os.path.dirname(__file__), "helvR12.bdf"),
    ]

    for path in candidate_paths:
        if not os.path.isfile(path):
            continue
        try:
            font.LoadFont(path)
            return path
        except Exception:
            continue

    raise RuntimeError("Unable to load font. Tried: " + ", ".join(candidate_paths))


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t",
            "--text",
            help="The text to scroll on the RGB LED panel",
            default="-1",
        )

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font_path = load_font_with_fallback(font)
        print(f"Using font: {font_path}")
        text_color = graphics.Color(0, 128, 255)
        pos = offscreen_canvas.width

        without_hold = int(self.args.text)
        school_day = get_school_day_from_day_finder()
        if not school_day:
            school_day = is_school_day()
            if "Error" in school_day:
                print(school_day)
                school_day = ""

        now = datetime.now()
        school_day_ended = now.hour > 15 or (now.hour == 15 and now.minute >= 30)
        if without_hold == 0 and school_day and not school_day_ended:
            without_hold -= 1

        my_text = get_board_output(without_hold, school_day)
        stored_day = date.today().strftime("%Y-%m-%d")

        count = 0
        while True:
            offscreen_canvas.Clear()
            text_len = graphics.DrawText(offscreen_canvas, font, pos, 14, text_color, my_text)

            pos -= 1
            if pos + text_len < 0:
                pos = offscreen_canvas.width

            time.sleep(0.025)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            count += 1
            if count > 12000:
                count = 0

                date_today = date.today().strftime("%Y-%m-%d")
                latest_school_day = get_school_day_from_day_finder()
                if not latest_school_day:
                    latest_school_day = is_school_day()
                    if "Error" in latest_school_day:
                        print(latest_school_day)
                        latest_school_day = school_day
                school_day = latest_school_day

                current_time = datetime.now()
                current_hour = current_time.hour
                current_minute = current_time.minute

                if school_day and not school_day_ended:
                    if current_hour > 15 or (current_hour == 15 and current_minute >= 30):
                        without_hold += 1
                        school_day_ended = True

                if school_day and (current_hour < 15 or (current_hour == 15 and current_minute < 30)):
                    school_day_ended = False

                if date_today != stored_day:
                    stored_day = date_today

                my_text = get_board_output(without_hold, school_day)


def get_calendar() -> str:
    """tries to open calendar from data folder

    Will make call to icalendar but only if we have never made the calendar
    OR calendar is not current. Should update calendar once a month.

    Returns:
        bool: if it was successful or not
    """
    calendar = ""
    try:
        with open("data/calendar.txt", 'r') as reader:
            full_calendar = reader.read()
    except FileNotFoundError as e:
        print(e)
    return calendar

def is_school_day() -> str:
    """ returns whether it's a school day according to the calendar.
    
    Returns:
        is_school_day: will return 'A DAY' or 'B DAY' if it's a school day
            or empty string if it isn't"""
    is_school_day = ""
    # get school calendar
    # TZ = timezone("America/Los_Angeles")
    date = datetime.now() + timedelta(days=0)
    datefor = "%s" % date.strftime("%Y-%m-%d")
    cur_year, cur_month, cur_day = datefor.split("-")
    events = []
    path_to_ics_file = "https://www.hsd.k12.or.us/fs/calendar-manager/"
    path_to_ics_file += "events.ics?calendar_ids=6"

    # set start and stop time
    dtend = False
    dtstart = False

    # get calendar feed
    try:
        r = re.get(path_to_ics_file)
        gcal = Calendar.from_ical(r.text)
        for event in gcal.walk("VEVENT"):
            in_range = within_range(event, datefor)
            if not in_range:
                continue
            else:
                print()
            if "A Day" in str(event["SUMMARY"]):
                # Get the start time
                start_date = event["DTSTART"].dt
                print()
            if "DTSTART" in event:
                try:
                    dtstart = event["DTSTART"].dt
                except Exception:
                    dtstart = False
            if "DTEND" in event:
                try:
                    dtend = event["DTEND"].dt
                except Exception:
                    dtend = False
            if dtstart or dtend:
                if datefor in "%s" % dtstart or datefor in "%s" % dtend:
                    # it's today, let's add the stuff
                    summary = str(event["SUMMARY"])
                    day = str(event['DTSTART'].dt.day)
                    same_day = day in datefor[-3:]
                    if same_day and "A DAY" in summary.upper() or same_day and "B DAY" in summary.upper():
                        print("We have a school day")
                        is_school_day = summary.upper()
                        return is_school_day
    except Exception as ex:
        return f"Error {ex}"
    
    return is_school_day

def within_range(event, target_date):
    # Let's only check for A or B day
    # IF it's an A or B day, I need to have a start month and an until and an interval

    summary = event["SUMMARY"]
    summary = str(summary).lower()
    a_or_b_day = summary.lower() in ["a day", "b day"]


    start_date = event["DTSTART"].dt
    start_year = start_date.year
    start_month = start_date.month
    start_day = start_date.day

    end_date = event["DTEND"].dt
    end_year = end_date.year
    end_month = end_date.month
    end_day = end_date.day

    date_parts = [int(x) for x in target_date.split("-")]
    cur_year, cur_month, cur_day = date_parts

    if a_or_b_day and start_year > 2025:
        # Get r_rules
        r_rules = event.rrules
        if len(r_rules) > 1:
            print()
        elif r_rules:
            r_rules = r_rules[0]
            frequency = r_rules["FREQ"][0]
            until = r_rules["UNTIL"][0]
            until_month = until.month
            until_day = until.day
            if until_month < cur_month:
                return False
            interval = int(r_rules["INTERVAL"][0])
        else:
            print("no RRULES")
    

    within_range = (cur_year == start_year and cur_month == start_month and
                    cur_day >= start_day and
                    cur_day <= end_day)
    return within_range


def get_board_output(without_hold: int, schoolday: str) -> str:
    """returns text for the readerboard.

    Args:
        without_hold: number of complete school days where we had no hold.
        schoolday: the summary for the day from the school calendar (this)
            comes from is_school_day() function.
    Returns:
        message: text displaying the day and # of days without a hold
    """
    # Display current time
    message = f"Current Time: {datetime.now().strftime('%I:%M %p')}.  "
    if schoolday:
        if schoolday == "A DAY":
            day = "an A"
        else:
            day = "a B"
            schoolday = False
        message += f"  Today is {day} day.    "
    else:
        message += "  There is no school today."
    
    if without_hold == -1:
        message += "  Days without a hold: 0."
    else:
        message += f"  Days without a hold: {without_hold}.  "
    
    # Get some other fun details
    days_text = days_until()
    message += days_text
    return message



# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()