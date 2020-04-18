# import statements
# import requests, icalendar
# from ics import Calendar
from datetime import date
import datetime

class Schedule:
  monday_schedule = {
    1: {"start":"08:30:00", "end":"10:02:00"},
    2: {"start":"10:08:00", "end":"11:40:00"},
    "Lunch": {"start":"11:40:00", "end":"12:20:00"},
    3: {"start":"12:24:00", "end":"13:52:00"},
    4: {"start":"13:58:00", "end":"15:30:00"}}
  tuesday_schedule = monday_schedule
  thursday_schedule = monday_schedule
  wednesday_schedule = {
    1: {"start":"09:00:00", "end":"10:25:00"},
    2: {"start":"10:31:00", "end":"11:56:00"},
    "Lunch":  {"start":"11:56:00", "end":"12:28:00"},
    3: {"start":"12:34:00", "end":"13:59:00"},
    4: {"start":"14:05:00", "end":"15:30:00"}}
  friday_schedule = {
    1: {"start": "08:30:00", "end":"09:58:00"},
    2: {"start":"09:59:00", "end":"11:22:00"},
    "Access": {"start":"11:28:00", "end":"11:58:00"},
    "Lunch": {"start":"11:58:00", "end":"12:32:00"},
    3: {"start": "12:38:00", "end":"14:01:00"},
    4: {"start": "14:07:00", "end":"15:30:00"}}
  weekly_schedule = {
    "Monday": monday_schedule,
    "Tuesday": tuesday_schedule,
    "Wednesday": wednesday_schedule,
    "Thursday": thursday_schedule,
    "Friday": friday_schedule,
    "Saturday": "It's Saturday. There are no classes.",
    "Sunday": "It's Sunday. There are no classes."
  }
  current_classes = (
    "No class in session",
    "Video Game Design 1-3", 
    "Prep",
    "Robotics",
    "Programming 1 & 2",
    "Prep",
    "Programming 1 & 2",
    "Video Game Design 1-3",
    "Research & Development") # current_classes[1]
  def get_today(self):
    now = datetime.datetime.now()
    today = now.strftime("%A")
    return today

  def get_todays_schedule(self):
    # get day of the week
    # use that to return the schedule for the day
    today = self.get_today()
    return Schedule.weekly_schedule[today]
  
  def get_schedule(self, day):
    return Schedule.weekly_schedule[day]

  def get_day_one_or_two(self, day_string):
    output = 0
    if "DAY 1" == day_string:
      output = 1
    elif "DAY 2" == day_string:
      output = 2
    return output
  def get_current_period(self, day_of_week, now, day=1):
    output = 0
    # get the hour and minute
    current_time = now.strftime("%H:%M:%S")
    # Get the schedule for the day
    schedule = self.get_schedule(day_of_week)
    # Loop through the schedule for that day
    # if the current time is between the start 
    # and stop of that class, get the period
    for i in schedule:
      s_start = schedule[i]['start']
      s_end = schedule[i]['end']
      if current_time > s_start and current_time < s_end:
        # if it's a day 1 return the period
        # otherwise return the period + 4 (it's a day 2)
        if day == 1:
          return i 
        else:
          return i + 4
    # If we're out of the loop, 
    # then we are not within the day's schedule, 
    # so we return 0 
    return output

  def get_class(self, period):
    return self.current_classes[period]
# Main scope
if __name__ == "__main__":
  s = Schedule();
  today = s.get_today()
  print("Today is {}".format(today))
  print("Today's schedule is {}".format(s.get_schedule(today)))
  print("Running get_todays_schedule results in {}".format(s.get_todays_schedule()))
  todays_schedule = s.get_schedule(today)
  print("\nLet's loop through today's schedule, which is type:{}".format(type(todays_schedule)))
  for i in todays_schedule:
    print("From {} to {}.".format(
      todays_schedule[i]['start'], todays_schedule[i]['end']))
  # Test times
  # mon = s.get_schedule("Monday")
  # mon_1 = mon[1]
  # mon_1_start = mon_1["start"]
  # mon_1_end = mon_1["end"]

  # print("1st period starts at {} and ends at {}".format(mon_1_start, mon_1_end))
  # print("1st period start is less than 1st period end == {}".format(mon_1_end>mon_1_start))
  
  today = s.get_today()
  schedule = s.get_schedule(today)
  now = datetime.datetime.now()
  # print("now[:2] = {}".format(now[:2]))
  print("today is {}, schedule is \n{}\nnow is {}".format(
    today, schedule, now))
  c_class = s.get_current_period(today, schedule, now)
  print ("The current class is {}.".format(c_class))
  input("Press enter to quit")