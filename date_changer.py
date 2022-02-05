import os, os.path
import datetime
import time
import pyexiv2
import sys


def modify_date(folder="images"):
    image_paths = os.listdir(folder)

    for image_path in image_paths:
        if image_path[0] != ".":
            print("Processing image: ", image_path)
            fullpath = f"{folder}/{image_path}"
            
            image = pyexiv2.Image(fullpath)
            dt = image.read_exif()['Exif.Image.DateTime'].split(' ')
            year, month, day = dt[0].split(':')
            hour, minute, second = dt[1].split(':')
            date = datetime.datetime(year=int(year), month=int(month), day=int(day), \
                hour=int(hour), minute=int(minute), second=int(second))
            new_time = time.mktime(date.timetuple())
            
            print("Changing modified date from", time.ctime(os.path.getmtime(fullpath)), "to", time.ctime(new_time))
            os.utime(fullpath, (new_time, new_time))


if __name__ == "__main__":
    folder = "images"
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    modify_date(folder)
