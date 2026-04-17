#!/usr/bin/python3
# # day_finder.py
# a Python script to determine whether it's a day 1, 2, or weekend

# import statements
import requests
import icalendar
from icalendar import Calendar, Event
from datetime import date
from datetime import datetime
import os
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

def get_current_day():
    url = "https://www.hsd.k12.or.us/fs/calendar-manager/events.ics?calendar_ids=6"
    res = requests.get(url)
    calendar = icalendar.Calendar.from_ical(res.text)
    output = []
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
        with open('current_calendar.ics', 'r') as cal:
            current_cal = Calendar(cal.read())

            # Check to make sure the calendar is current

            # If not, pull the calendar again

    except FileNotFoundError:
        # pull the online calendar
        current_cal = get_calendar()

        # add required data
        current_cal.add('prodid', '-//Current_year Calendar//')
        current_cal.add('version', '0.1')

        current_cal.add('x-school-year', school_year)
        
        # clean calendar of old years
        start_year, end_year = school_year.split("-")

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
            print("We stopped here.")
        # save calendar


    
    

    
    
    # Create a calendar for the current year
    current_cal = Calendar()

    
    return current_cal


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
    day_one_or_two = get_current_day()
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
