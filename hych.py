from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint

def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days = diff_days)

def prepare_birthday(text: str):
    bd = datetime.strptime(text, "%d, %m, %Y")
    birthday_date = bd.replace(year=datetime.now().year).date()
    
    return birthday_date

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)
    birthday_next_week_users = [user for user in users if start_period <= prepare_birthday(user["birthday"]) <= end_period]

    for user in birthday_next_week_users:
        current_bd = prepare_birthday(user["birthday"])
        if current_bd.weekday() in (5,6):
            birthdays["Monday"].append(user["name"])
        else:
            birthdays[current_bd.strftime("%A")].append(user["name"])

    return birthdays

if __name__ == "__main__":
    users = [{"name": "Alex", "birthday": "15, 3, 1991"},
            {"name": "Petya", "birthday": "16, 3, 1992"},
            {"name": "Yehor", "birthday": "17, 3, 1993"},
            {"name": "Kolya", "birthday": "18, 3, 1994"},
            {"name": "Stepan", "birthday": "19, 3, 1995"},
            {"name": "Petro", "birthday": "20, 3, 1996"},
            {"name": "Stas", "birthday": "21, 3, 1997"},
            {"name": "Ivan", "birthday": "22, 3, 1998"},
            {"name": "Alex1", "birthday": "19, 3, 1991"},
            {"name": "Petya1", "birthday": "20, 3, 1992"},
            {"name": "Yehor1", "birthday": "25, 3, 1993"},
            {"name": "Kolya1", "birthday": "26, 3, 1994"},
            {"name": "Stepan1", "birthday": "27, 3, 1995"},
            {"name": "Petro1", "birthday": "28, 3, 1996"},
            {"name": "Stas1", "birthday": "29, 3, 1997"},
            {"name": "Ivan1", "birthday": "30, 3, 1998"}]

    
    pprint(get_birthdays_per_week(users))