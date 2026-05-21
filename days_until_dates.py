from datetime import date
from datetime import datetime

def days_until() -> str:
    msg = ""
    
    for target in TARGET_DATES:
        event, target_date = target.values()
        # print(event, target_date)
        today = date.today()
        year = today.year
        month = today.month
        day = today.day
        current_day = datetime(year, month, day)
        target_day = datetime.strptime(target_date, date_format)
        days_to_go = target_day - current_day
        
        if "Summer Vacation" in event or "Spring Break" in event or "Focus Program" in event:
            date_format = "%Y-%m-%d %H:%M"
            today = datetime.now()
            hour = today.hour
            minute = today.minute
            current_day = datetime(year, month, day, hour, minute)
        else:
            date_format = "%Y-%m-%d"

       
        if days_to_go.days < 0:
            continue
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
                msg += f"    {days_left} days, {hours} hours, and {minutes} minutes left until"
                msg += " College Career Pathways Night.    "
        elif "Spring Break" in event:
            full_seconds = days_to_go.seconds
            hours, minutes = get_hours_minutes(full_seconds)
            msg += f"       {days_left} days, {hours} hours, and {minutes} minutes left until "
            msg += "Spring Break"
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
    {"event": "Jagapalooza",
    "date": "2026-05-22"},
    {"event": "Focus Program Night",
    "date": "2026-05-27 18:00"},
    {"event": "Class of '26 Graduation",
    "date": "2025-06-04"},
    {"event": "Summer Vacation begins.",
    "date": "2026-06-11 12:30"},
    {"event": "School comes along just to end it",
     "date":  "2026-09-02"}
]

if __name__ == "__main__":
    pass