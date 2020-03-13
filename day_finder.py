# day_finder.py
# a Python script to determine whether it's a day 1, 2, or weekend

# import statements
import requests, icalendar
from ics import Calendar
from datetime import date

# get today's date
today = date.today()

# Try and calculate if it's a day 1 or day 2
def isDayOneOrTwo():
    # scrape the Century Website calendar to see if it's
    # a day 1 or day 2 (or weekend)
    # returns a string day 1, day 2, weekend
    # Can I read data from the CHS Calendar for the current day?
    day = get_current_day()
    # display(day)
    
    # type(calendar)
    print("Today is a " + day)

def get_current_day():
    url = "https://www.hsd.k12.or.us/site/handlers/icalfeed.ashx?MIID=37"
    res = requests.get(url)
    calendar = icalendar.Calendar.from_ical(res.text)
    output = []
    today = date.today()
    for event in calendar.walk('vevent'):
        summary = event.get('summary')
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
    isDayOneOrTwo()
    input("\nPress enter to quit.")
