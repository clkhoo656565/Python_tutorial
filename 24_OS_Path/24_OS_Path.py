import os
from os import path
import datetime
from datetime import date, time, timedelta
import platform
import time

def main():
    print(f'The current OS is {os.name}')
    print(f'The current OS version is {platform.version()}')
    print(f'Item path: {str(path.realpath("Airbnb_data.csv"))}')
    print(f'Item exists: {str(path.exists("Airbnb_data.csv"))}')
    print(f'Item is a file: {str(path.isfile("Airbnb_data.csv"))}')
    print(f'Item is a directory: {str(path.isdir("Airbnb_data.csv"))}')
    print(f'Item path and name: {str(path.split(path.realpath("Airbnb_data.csv")))}')

    t = time.ctime(path.getmtime("Airbnb_data.csv"))
    print(f'The modification time of the Airbnb_data.csv file: {t}')
    print(f'The modification time of the Airbnb_data.csv file: {datetime.datetime.fromtimestamp(path.getmtime("Airbnb_data.csv"))}')

    #Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("Airbnb_data.csv")
    )
    print(f'It has been {str(td)} since the file was modified')
    print(f'Or {str(td.total_seconds())} seconds ')

if __name__ == "__main__":
    main()