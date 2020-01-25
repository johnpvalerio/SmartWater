import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return run_time

    return wrapper_timer


@timer
def water_read():
    while True:
        with open('WaterInput.txt') as file:
            data = file.read()
            if data != '0':
                continue
            else:
                return
