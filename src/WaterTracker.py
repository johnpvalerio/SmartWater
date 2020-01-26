from datetime import date
import json
from tkinter import *
import tkSnack

def update_user():
    with open('WaterInfo.JSON', 'w') as file:
        json.dump(file, setup(), indent=4)

def setup():
    db = {}
    temp = {}
    temp['total_intake'] = 0
    temp['chug_pb'] = 0
    temp['freq'] = 0
    db[date.today()] = temp

    return db

def sound(sound_clip_wav):
    root = Tk()
    tkSnack.initializeSnack(root)
    snd = tkSnack.Sound()
    snd.read(sound_clip_wav)
    snd.play(blocking=1)
    