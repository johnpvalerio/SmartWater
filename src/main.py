from src.WaterReader import water_read
from src.WaterTracker import setup

if __name__ == '__main__':
     while True:
          output = water_read()
          print(output)
          setup()
