from src.WaterReader import water_read
from src.WaterTracker import setup, load_db, update_user

if __name__ == '__main__':
    load_db()
    # update_user()
    while True:
        output = water_read()
        print(output)
        update_user(output)
