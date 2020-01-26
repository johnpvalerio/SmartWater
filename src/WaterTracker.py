import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
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
    # todo: daily_intake update
    db[str(date.today())]['freq'] += 1
    db[str(date.today())]['total_intake'] += water_calc(usr_time)


def load_db():
    global db
    with open('WaterInfo.json', 'r') as r_f:
        temp = json.load(r_f)
    for k, v in temp.items():
        db[datetime.datetime.strptime(k, '%Y-%m-%d')] = v


def save_db():
    with open('WaterInfo.json', 'w', encoding='utf-8') as w_f:
        db = setup()
        json.dump(db, w_f, indent=4)


def setup():
    db = {}
    for i in reversed(range(10)):
        temp = {'total_intake': 0, 'daily_intake': 0, 'chug_pb': 0, 'freq': 0}
        db[str(date.today() - timedelta(days=i))] = temp
    # print(db)
    return db


def graph():
    lines = []
    vals = []
    line = 0
    dates = [d for d in db]

    for d, val in db.items():
        vals.append(val['total_intake'])
    print(len(dates))
    print(len(vals))
        # lines.append(line)
    plt.plot(dates, vals)
    plt.grid(True)  # grid lines
    plt.title("Time series of total water intake")  # title
    plt.xticks(ticks=dates)  # display only given dates

    fig = plt.gcf()
    fig.autofmt_xdate()  # might delete
    plt.show()
    plt.draw()
    fig.savefig('graph.png', bbox_inches='tight')
