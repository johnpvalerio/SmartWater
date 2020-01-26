import functools
import time
import serial
import struct

arduinoSerialData = serial.Serial('/dev/ttyACM1', 9600)


def timer(func):
    @functools.wraps(func)
    def wrapper_timer():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        return run_time

    return wrapper_timer


@timer
def water_read():
    while True:
        data = (int(float(arduinoSerialData.readline().decode('utf-8'))))
        if data != 0:
            continue
        else:
            return
