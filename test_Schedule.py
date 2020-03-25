import pytest 
import Schedule 
import datetime
from datetime import date
from datetime import datetime

s = Schedule.Schedule()

def test_get_schedule_mon():
  mon = s.get_schedule("Monday")
  results = mon[1]
  expected = {"start":"08:30:00", "end":"10:02:00"}
  assert expected == results

def test_start_v_end():
  mon = s.get_schedule("Monday")
  mon_start = mon[1]["start"]
  mon_end = mon[1]["end"]
  results = mon_end > mon_start
  expected = True
  assert expected == results

def test_get_schedule_sat():
  sat = s.get_schedule("Saturday")
  results = sat
  expected = "It's Saturday. There are no classes."
  assert expected == results

def test_get_today():
  now = datetime.now()
  expected = now.strftime("%A")
  print("In test_get_today, and today is {}".format(expected))
  results = s.get_today()
  print("Same test, and the results are {}".format(results))
  assert expected == results

def test_get_current_period_mon_1():
  # set day to Monday
  day_of_week = "Monday"
  # set now to 9:30am
  # now = datetime.date(2020, 3, 23, 9,30)
  now = datetime.strptime('2020-03-23 09:30:23', '%Y-%m-%d %H:%M:%S')
  day = 1
  expected = 1
  results = s.get_current_period(day_of_week, now, day)
  assert expected == results

def test_get_current_period_mon_7():
  # set day to Monday
  day_of_week = "Monday"
  # set now to 1:30pm
  now = datetime.strptime('2020-03-23 13:30:23', '%Y-%m-%d %H:%M:%S')
  day = 2
  expected = 7
  results = s.get_current_period(day_of_week, now, day)
  assert expected == results

def test_get_current_period_wed_0():
  # set day 
  day_of_week = "Wednesday"
  # set now to 9:30am
  # now = datetime.date(2020, 3, 23, 9,30)
  now = datetime.strptime('2020-03-25 08:30:23', '%Y-%m-%d %H:%M:%S')
  day = 1
  expected = 0
  results = s.get_current_period(day_of_week, now, day)
  assert expected == results

def test_get_current_period_tues_day2_0():
  # set day 
  day_of_week = "Tuesday"
  # set now to 3:30pm
  # now = datetime.date(2020, 3, 24, 3,30)
  now = datetime.strptime('2020-03-24 15:30:23', '%Y-%m-%d %H:%M:%S')
  day = 2
  expected = 0
  results = s.get_current_period(day_of_week, now, day)
  assert expected == results

def test_get_class_programming_1():
  expected = "Programming 1 & 2"
  results = s.get_class(4)
  assert expected == results

def test_get_class_programming_2():
  expected = "Programming 1 & 2"
  results = s.get_class(6)
  assert expected == results