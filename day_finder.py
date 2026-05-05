#!/usr/bin/python3
# # day_finder.py
# a Python script to determine whether it's a day 1, 2, or weekend

# import statements
import requests
import icalendar
from icalendar import Calendar, Event
from datetime import date, datetime, timezone
import os
import pytz
import Schedule as s
# Create a CHS Schedule Object

# get today's date
today = date.today()

# Try and calculate if it's a day 1 or day 2
def isDayOneOrTwo():
    # scrape the Century Website calendar to see if it's
    # a day 1 or day 2 (or weekend)
    # returns a string day 1, day 2, weekend
    # Can I read data from the CHS Calendar for the current day?
    day = get_current_day()

    # type(calendar)
    print("Today is a " + day)

def get_daily_summaries():
    calendar = get_calendar()
    output = []
    today = date.today()
    c_month = today.month
    c_day = today.day
    print("Month = {}\tDay = {}".format(c_month, c_day))
    for event in calendar.walk('vevent'):
        e_month = event['DTSTART'].dt.month
        e_day = event['DTSTART'].dt.day
        if e_month == c_month and e_day == c_day:
            summary = event.decoded('summary')
            summary = clean_summary(summary)
            input(summary)
            output.append(summary)
        
    return output

def get_calendar():
    url = "https://www.hsd.k12.or.us/fs/calendar-manager/events.ics?calendar_ids=6"
    res = requests.get(url)
    calendar = icalendar.Calendar.from_ical(res.text)
    return calendar

def clean_summary(text):
    if isinstance(text, bytes):
        return text.decode('utf-8')
    return text

def is_weekday(current_day):
    """ receives a current_day object -> bool """
    return date.weekday(current_day) < 5

def get_current_day(calendar: Calendar) -> str:
    output = []

    ##############################
    # TODO: fix the A B conundrum
    ##############################
    today = date.today()
    for event in calendar.walk('vevent'):
        summary = event.get('summary')
        # input(summary)
        e_month = event['DTSTART'].dt.month
        e_day = event['DTSTART'].dt.day
        c_month = today.month
        c_day = today.day
        if e_month == c_month and e_day == c_day:
            if 'DAY' in summary:
                return summary
    
    # if we're still in the loop, there must not be a DAY 1 or DAY 2
    # it must be the weekend
    return "No School Day"


def get_current_calendar(now: datetime) -> icalendar:
    """returns a calendar for just the current school year"""
    school_year = get_school_year(now)

    # Try and open current_calendar file (if it exists)
    try:
        with open('current_calendar.ics', 'r', encoding='utf-8') as cal:
            calendar_text = cal.read()

            # convert the text to a calendar
            current_cal = Calendar.from_ical(calendar_text)
            
            # Check to make sure the calendar is current
            last_modified = get_last_modified(current_cal)
            modified_month = last_modified[5:7]
            modified_month = int(modified_month)
            current_month = now.strftime("%m")
            current_month = int(current_month)

            # if the current month is past the modified month - get a new calendar
            if current_month > modified_month:
                # throwing the error forces us to make a new calendar
                # this will only happen once a month
                raise FileNotFoundError
            
            # Success! return the calendar
            return current_cal

    except FileNotFoundError:
        # create & config our adjusted calendar
        adjusted_cal = Calendar()
        adjusted_cal.add('prodid', '-//Current_year Calendar//')
        adjusted_cal.add('prodid', '-//Current_year Calendar//')
        adjusted_cal.add('version', '0.1')
        adjusted_cal.add('x-school-year', school_year)

        # pull the online calendar
        current_cal = get_calendar()
        
        # clean calendar of old years
        start_year, end_year = [int(x) for x in school_year.split("-")]

        # create a new calendar
        for event in current_cal.walk('vevent'):
            # get year and month
            # add only events that are within this school year (August to July)
            e_year = event['DTSTART'].dt.year
            e_month = event['DTSTART'].dt.month
            if e_year < start_year or e_year > end_year:
                continue
            elif e_year == start_year and e_month < 8:
                continue
            elif e_year == end_year and e_month > 7:
                continue
            adjusted_cal.add_component(event)
        
        # save calendar
        adjusted_events = adjusted_cal.events
        try:
            with open('current_calendar.ics', 'wb') as cal:
                cal.write(adjusted_cal.to_ical())
        except Exception as ex:
            print(ex)
        return adjusted_cal

def get_last_modified(calendar: Calendar) -> str:
    """get the last time the calendar was modified or set it and return it"""
    last_modified = calendar.LAST_MODIFIED
    if not last_modified:
        # get now in UTC time
        current_date = datetime.now(pytz.UTC)
        calendar.LAST_MODIFIED = current_date
        current_date = current_date.isoformat()
        last_modified = current_date
    return last_modified


def get_school_year(now):
    cur_month = now.month
    cur_year = now.year
    if cur_month < 8:
        school_year = f"{cur_year-1}-{cur_year}"
    else:
        school_year = f"{cur_year}-{cur_year+1}"
    return school_year


# Main scope
if __name__ == "__main__":
    
    schedule = s.Schedule()
    
    # Get the current time
    now = datetime.now()
    current_year_cal = get_current_calendar(now)

    ###################################################################
    # TODO: Modify get_current_day by passing it a current calendar
    ###################################################################

    day_one_or_two = get_current_day(current_year_cal)
    day_of_week = schedule.get_today()
    period = schedule.get_current_period(day_of_week, now, day_one_or_two)
    c_class = schedule.get_class(period)
    print("Today is a {}".format(day_one_or_two))
    print("The current class is {}".format(c_class))
    input("Press enter to get today's announcements.")
    announcements = get_daily_summaries()
    # for a in announcements:
    #     print(a)
    input("\nPress enter to quit.")
