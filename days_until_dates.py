from datetime import date
from datetime import datetime
from datetime import timedelta


def days_until(is_school_day) -> str:
    from days_until_dates import TARGET_DATES
    msg = ""
    
    for target in TARGET_DATES:
        event, target_date = target.values()
        # print(event, target_date)
        today = date.today()
        year = today.year
        month = today.month
        day = today.day
        current_day = datetime(year, month, day)
        if "Summer Vacation" in event:
            date_format = "%Y-%m-%d %H:%M"
            today = datetime.now()
            hour = today.hour
            minute = today.minute
            current_day = datetime(year, month, day, hour, minute)
        else:
            date_format = "%Y-%m-%d"
        target_day = datetime.strptime(target_date, date_format)

        
        days_to_go = target_day - current_day
        days_left = days_to_go.days
        if "Summer Vacation" in event:
            # now = datetime.now()
            full_seconds = days_to_go.seconds
            hours, minutes = get_hours_minutes(full_seconds)
            msg += f"       {days_left} days, {hours} hours, and {minutes} minutes left until "
            msg += "Summer Vacation.    "
        elif days_left == 1:
            msg += f"       {days_left} day left until {event}!"
        elif days_left > 1:
            msg += f"    {days_left} days until {event}.       "
        elif days_left == 0:
            msg += f"      Today is {event}!"
        else:
            continue
    return msg


def get_hours_minutes(seconds):
    return seconds//3600, (seconds//60) % 60


TARGET_DATES = [
    {"event": "Graduation",
    "date": "2024-06-08"},
    {"event": "Summer Vacation",
    "date": "2024-06-13 12:30"},
    {"event": "Summer School Officially Ends",
    "date": "2024-07-03"},
    {"event": "The 4th of July",
    "date": "2024-07-04"},
    {"event": "First Day of Fall Practice",
    "date": "2024-08-19"},
    {"event": "CHS Open House",
    "date": "2024-08-28"}
]

if __name__ == "__main__":
    pass