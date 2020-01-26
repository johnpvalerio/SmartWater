from src.WaterReader import water_read
from src.WaterTracker import setup, load_db, update_user, save_db, graph

if __name__ == '__main__':
    load_db()
    # save_db()
    graph()
    # while True:
    #     output = water_read()
    #     print(output)
    #     update_user(output)
