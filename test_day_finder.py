import pytest 
import day_finder 
import datetime
from datetime import date

def test_clean_summary_one():
  text = bytes('fred', 'utf-8')
  results = day_finder.clean_summary(text)
  expected = "fred"
  assert expected == results

def test_is_weekday_for_true():
  wed = datetime.datetime(2020, 3, 18)
  # 3/18/20 was a Wednesday 
  results = day_finder.is_weekday(wed)
  expected = True
  assert expected == results

def test_is_weekday_for_false():
  sat = datetime.datetime(2020, 3, 21)
  # 3/21/20 was a Saturday, not a weekday
  results = day_finder.is_weekday(sat)
  expected = False
  assert expected == results

def test_get_period_one():
  expected = 1
