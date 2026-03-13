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
        if "Summer Vacation" in event or "Focus Program" in event:
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
            full_seconds = days_to_go.seconds
            hours, minutes = get_hours_minutes(full_seconds)
            if days_left >= 0:
                msg += f"       {days_left} days, {hours} hours, and {minutes} minutes left until "
                msg += "Summer Vacation.    "
        elif "Focus Program Night" in event:
            full_seconds = days_to_go.seconds
            hours, minutes = get_hours_minutes(full_seconds)
            if days_left > 0 and hours > 0 and minutes > 0:
                msg += f"	    {days_left} days, {hours} hours, and {minutes} minutes left until"
                msg += " Focus Program Night.    "
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
    {"event": "Winter Break begins",
    "date": "2024-12-21"},
    {"event": "the end of First Semester",
    "date": "2025-01-31"},
    {"event": "Oregon Game Project Challenge",
    "date": "2025-05-10"},
    {"event": "Focus Program Night",
    "date": "2025-05-28 18:00"},
    {"event": "Class of '25 Graduation",
    "date": "2025-06-04"},
    {"event": "Summer Vacation begins.",
    "date": "2025-06-12 12:25"},
    {"event": "School comes along just to end it",
     "date":  "2025-09-04"}
]

if __name__ == "__main__":
    pass