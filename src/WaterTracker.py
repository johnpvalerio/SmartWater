import copy
import datetime
from datetime import date, timedelta
from random import randint

import matplotlib.pyplot as plt
import json

db = {}
user1 = 1234
user2 = 5678

def water_calc(time):
    flow_rate = 1.44
    return time * flow_rate


def update_user(usr_time):
    last_rec = db[str(user1)][str(date.today() - timedelta(days=1))]
    pb = last_rec['chug_pb']
    if pb < usr_time:
        db[str(user1)][str(date.today())]['chug_pb'] = usr_time
    # todo: daily_intake update
    db[str(user1)][str(date.today())]['freq'] += 1
    db[str(user1)][str(date.today())]['total_intake'] += water_calc(usr_time)


def load_db():
    global db
    with open('WaterInfo.json', 'r') as r_f:
        temp = json.load(r_f)
    for user, v in temp.items():
        db[user] = {}
        for d, i in v.items():
            db[user][datetime.datetime.strptime(d, '%Y-%m-%d')] = i


def save_db():
    with open('WaterInfo.json', 'w', encoding='utf-8') as w_f:
        db = setup()
        json.dump(db, w_f, indent=4)


def setup():
    db = {}
    temp2 = {}
    for i in reversed(range(10)):
        r_int = randint()
        temp = {'total_intake': randint(10-i, ), 'daily_intake': 0, 'chug_pb': 0, 'freq': 0}
        temp2[str(date.today() - timedelta(days=i))] = temp
        t2 = copy.copy(temp2)
        db[user1] = temp2
        db[user2] = t2
    # print(db)
    return db


def graph():
    lines = []
    vals1 = []
    vals2 = []
    line = 0
    dates = []

    for k,v in db[str(user1)].items():
        vals1.append(v['total_intake'])
        dates.append(k)
    print(len(dates))
    print(len(vals1))
    print(dates)
    print(vals1)
    plt.plot(dates, vals1)
    for k,v in db[str(user2)].items():
        vals2.append(v['total_intake'])
    plt.plot(dates, vals2)
    # for user, v in db.items():
    #     for d, val in v.items():
    #         print(d)
    #         print(val)
    #
    # vals.append(val['total_intake'])

    # plt.plot(dates, vals)
    plt.grid(True)  # grid lines
    plt.title("Time series of total water intake")  # title
    plt.xticks(ticks=dates)  # display only given dates

    fig = plt.gcf()
    fig.autofmt_xdate()  # might delete
    plt.show()
    plt.draw()
    fig.savefig('graph.png', bbox_inches='tight')
