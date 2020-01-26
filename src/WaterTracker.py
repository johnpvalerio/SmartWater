import datetime
from datetime import date, timedelta
import json

db = {}


def water_calc(time):
    flow_rate = 1.44
    return time * flow_rate


def update_user(usr_time):
    last_rec = db[str(date.today() - timedelta(days=1))]
    pb = last_rec['chug_pb']
    if pb < usr_time:
        db[str(date.today())]['chug_pb'] = usr_time

    db[str(date.today())]['freq'] += 1
    db[str(date.today())]['total_intake'] += water_calc(usr_time)


def load_db():
    global db
    with open('WaterInfo.json', 'r') as r_f:
        temp = json.load(r_f)
    for k,v in db.items():
        db[datetime.strptime(k, '%m/%d/%y')]


def save_db():
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
