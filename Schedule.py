# import statements
import requests, icalendar
from ics import Calendar
from datetime import date
import datetime

class Schedule:
  monday_schedule = {
    1: {"start":"8:30:00", "end":"10:02:00"},
    2: {"start":"10:08:00", "end":"11:40:00"},
    "Lunch": {"start":"11:40:00", "end":"12:20:00"},
    3: {"start":"12:24:00", "end":"13:52:00"},
    4: {"start":"13:58:00", "end":"15:30:00"}}
  tuesday_schedule = monday_schedule
  thursday_schedule = monday_schedule
  wednesday_schedule = {
    1: {"start":"9:00:00", "end":"10:25:00"},
    2: {"start":"10:31:00", "end":"11:56:00"},
    "Lunch":  {"start":"11:56:00", "end":"12:28:00"},
    3: {"start":"12:34:00", "end":"13:59:00"},
    4: {"start":"14:05:00", "end":"15:30:00"}}
  friday_schedule = {
    1: {"start": "8:30:00", "end":"9:58:00"},
    2: {"start":"9:59:00", "end":"11:22:00"},
    "Access": {"start":"11:28:00", "end":"11:58:00"},
    "Lunch": {"start":"11:58:00", "end":"12:32:00"},
    3: {"start": "12:38:00", "end":"14:01:00"},
    4: {"start": "14:07:00", "end":"15:30:00"}}
  weekly_schedule = {
    "Monday": monday_schedule,
    "Tuesday": tuesday_schedule,
    "Wednesday": wednesday_schedule,
    "Thursday": thursday_schedule,
    "Friday": friday_schedule
  }
  def get_todays_schedule(self):
      # get day of the week
      # use that to return the schedule for the day
      now = datetime.datetime.now()
      today = now.strftime("%A")
      return Schedule.weekly_schedule[today]
