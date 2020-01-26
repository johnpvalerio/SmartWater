import datetime
from datetime import date, timedelta
import json

db = {}


def load_db():
    global db
    with open('WaterInfo.json', 'r') as r_f:
        db = json.load(r_f)


def update_user():
    with open('WaterInfo.json', 'w', encoding='utf-8') as w_f:
        # db = setup()
        json.dump(db, w_f, indent=4)


def setup():
    db = {}
    for i in reversed(range(10)):
        temp = {'total_intake': 0, 'chug_pb': 0, 'freq': 0}
        db[str(date.today() - timedelta(days=i))] = temp
    # print(db)
    return db
