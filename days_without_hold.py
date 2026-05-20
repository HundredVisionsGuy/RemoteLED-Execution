#!/usr/bin/env python
# Display a runtext with double-buffering.
# pipfrom samplebase import SampleBase
# from rgbmatrix import graphics
import time
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import requests as re
from icalendar import Calendar
from pytz import timezone
from days_until_dates import TARGET_DATES, get_hours_minutes, days_until


def is_weekday(day):
    return day in ("Mon", "Tue", "Wed", "Thu", "Fri")


# class RunText(SampleBase):
#     def __init__(self, *args, **kwargs):
#         super(RunText, self).__init__(*args, **kwargs)
#         self.parser.add_argument("-t", "--text",
#             help="The text to scroll on the RGB LED panel",
#             default="Hello world!")

#     def run(self):
#         offscreen_canvas = self.matrix.CreateFrameCanvas()
#         font = graphics.Font()
#         font.LoadFont("../../../../fonts/helvR12.bdf")
#         textColor = graphics.Color(0, 128, 255)
#         pos = offscreen_canvas.width
#         without_hold = int(self.args.text)
#         days_since_running = 0

#         # set up day info and get school day data
#         TZ = timezone("US/Pacific")
#         date = datetime.now() + timedelta(days=0)
#         datefor = "%s" % date.strftime("%Y-%m-%d")
#         start_date = date.today()
#         stored_day = start_date.strftime("%Y-%m-%d")
#         start_day = start_date.strftime("%a")
#         current_day = start_day
        
        
#         # is it a school day?
#         school_day = is_school_day()
#         school_day_ended = False

#         if without_hold == 0:
#             if school_day and start_date.hour <= 15 and start_date.minute < 30:
#                 without_hold -= 1
#         if without_hold == -1:
#             my_text = "  Days without a hold: 0.  "
#         else:
#             my_text = f"  Days without a hold: {without_hold}.  "
#         if school_day:
#             if school_day == "A DAY":
#                 day = "an A"
#             else:
#                 day = "a B"
#             my_text += f"  Today is {day} day.  "
            
#             current_hour = start_date.hour
#             current_minute = start_date.minute
#             print(my_text)
#             school_day_ended = False
#             if current_hour < 15 and current_minute < 30:
#                 school_day_ended = False
#                 print("School day is NOT over...yet.")
#             else:
#                 school_day_ended = True
#                 print("School day is already over.")
#         my_text += days_until(schoolday)

#         # initialize last recorded hour and minute
#         last_time = datetime.now()
#         last_hour = last_time.strftime("%H")
#         last_minute = last_time.strftime("%M")
#         count = 0
#         while True:
#             offscreen_canvas.Clear()
#             len = graphics.DrawText(offscreen_canvas, font, pos, 14,
#                 textColor, my_text)
            
#             # scroll text to the left (subtract pos by 1)
#             pos -= 1

#             # if we go off the screen (to the left) move it to the right of 
#             # the screen
#             if (pos + len < 0):
#                 pos = offscreen_canvas.width

#             time.sleep(0.025)
#             offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            
#             count += 1
#             if count > 12000:
#                 count = 0

#                 # check the date to see if it changed
#                 today = date.today()
#                 date_today = today.strftime("%Y-%m-%d")
#                 last_school_day = school_day
#                 school_day = is_school_day()
#                 print(school_day)

#                 # account for errors
#                 if "Error" in school_day:
#                     error_msg = school_day
#                     print(error_msg)
#                     school_day = last_school_day
#                 my_text = get_board_output(without_hold, school_day)

#                 # get current hour and minute
#                 current_time = datetime.now()
#                 current_hour = current_time.hour
#                 current_minute = current_time.minute

#                 # If it's a school day AND it's past 3:30pm
#                 if school_day and not school_day_ended:
#                     if current_hour >= 15 and current_minute > 30:
#                         if days_since_running >= 0:
#                             without_hold += 1
#                         my_text = get_board_output(without_hold, school_day)
                        
#                         school_day_ended = True
#                         print(f"The School day is now over. Days without hold: {without_hold}")
#                 if current_hour < 15 and current_minute < 30 and school_day:
#                     school_day_ended = False
#                     print("School day is NOT over...yet.")
#                 if date_today != stored_day:
#                     print(f"Today is {date_today}. We have a change in date")
#                     stored_day = date_today
#                     days_since_running += 1
                    
#                 print(f"Time: {current_time} date_today = {date_today} & stored_day = {stored_day}")
#                 print(f"Q: Is school day over? A: {school_day_ended} Days without hold: {without_hold}")

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
    TZ = timezone("US/Pacific")
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
    if schoolday:
        if schoolday == "A DAY":
            day = "an A"
        else:
            day = "a B"
            schoolday = False
        message = f"  Today is {day} day.    "
    else:
        message = "  There is no school today."
    if without_hold == -1:
        message += f"  Days without a hold: 0.   "
    else:
        message += f"  Days without a hold: {without_hold}.    "
    
    # Get some other fun details
    message += days_until(schoolday)
    return message



# Main function
if __name__ == "__main__":
    get_calendar()

    schoolday = is_school_day()
    output = days_until(schoolday)
    TZ = timezone("US/Pacific")
    date = datetime.now() + timedelta(days=0)
    datefor = "%s" % date.strftime("%Y-%m-%d")
    start_date = date.today()
    stored_day = start_date.strftime("%Y-%m-%d")
    start_day = start_date.strftime("%a")
    current_day = start_day
    
    
    # is it a school day?
    school_day = is_school_day()
    school_day_ended = False
    without_hold = -1
    if without_hold == 0:
        if school_day and start_date.hour <= 15 and start_date.minute < 30:
            without_hold -= 1
    if without_hold == -1:
        my_text = "  Days without a hold: 0.  "
    else:
        my_text = f"  Days without a hold: {without_hold}.  "
    if school_day:
        if school_day == "A DAY":
            day = "an A"
        else:
            day = "a B"
        my_text += f"  Today is {day} day.  "
        
        current_hour = start_date.hour
        current_minute = start_date.minute
        print(my_text)
        school_day_ended = False
        if current_hour < 15 and current_minute < 30:
            school_day_ended = False
            print("School day is NOT over...yet.")
        else:
            school_day_ended = True
            print("School day is already over.")
    my_text += days_until(schoolday)

    # initialize last recorded hour and minute
    last_time = datetime.now()
    last_hour = last_time.strftime("%H")
    last_minute = last_time.strftime("%M")
    print(my_text)