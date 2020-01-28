from WaterReader import water_read
from WaterTracker import setup, load_db, update_user, save_db, graph

if __name__ == '__main__':
    load_db()
    # setup()
    # save_db()
    
    while True:
        output = water_read()
        print(output)
        update_user(output)
        graph()
