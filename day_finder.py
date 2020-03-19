#!/usr/bin/python3
# # day_finder.py
# a Python script to determine whether it's a day 1, 2, or weekend

# import statements
import requests, icalendar
from ics import Calendar
from datetime import date

# Create a CHS Schedule Object
class Schedule:
  monday_schedule = {
    1: {"start":"8:30", "end":"10:02"},
    2: {"start":"10:08", "end":"11:40"},
    "Lunch": {"start":"11:40", "end":"12:20"},
    3: {"start":"12:24", "end":"13:52"},
    4: {"start":"13:58", "end":"15:30"}}
  tuesday_schedule = monday_schedule
  thursday_schedule = monday_schedule
  wednesday_schedule = {
    1: {"start":"9:00", "end":"10:25"},
    2: {"start":"10:31", "end":"11:56"},
    "Lunch":  {"start":"11:56", "end":"12:28"},
    3: {"start":"12:34", "end":"13:59"},
    4: {"start":"14:05", "end":"15:30"}}
  friday_schedule = {
    1: {"start": "8:30", "end":"9:58"},
    2: {"start":"9:59", "end":"11:22"},
    "Access": {"start":"11:28", "end":"11:58"},
    "Lunch": {"start":"11:58", "end":"12:32"},
    3: {"start": "12:38", "end":"14:01"},
    4: {"start": "14:07", "end":"15:30"}}
  weekly_schedule = {
    "Monday": monday_schedule,
    "Tuesday": tuesday_schedule,
    "Wednesday": wednesday_schedule,
    "Thursday": thursday_schedule,
    "Friday": friday_schedule
  }
  

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
    url = "https://www.hsd.k12.or.us/site/handlers/icalfeed.ashx?MIID=37"
    res = requests.get(url)
    calendar = icalendar.Calendar.from_ical(res.text)
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

def clean_summary(text):
    output = text.decode('utf-8')
    return output

def is_weekday(current_day):
    """ receives a current_day object -> bool """
    return date.weekday(current_day) < 5

def get_current_day():
    url = "https://www.hsd.k12.or.us/site/handlers/icalfeed.ashx?MIID=37"
    res = requests.get(url)
    calendar = icalendar.Calendar.from_ical(res.text)
    output = []
    today = date.today()
    for event in calendar.walk('vevent'):
        summary = event.get('summary')
        input(summary)
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


# Main scope
if __name__ == "__main__":
    # isDayOneOrTwo()
    # summaries = []
    # summaries = get_daily_summaries()
    # print(summaries)
    schedule = Schedule()
    print(schedule.monday_schedule[1]["start"])
    input("\nPress enter to quit.")
