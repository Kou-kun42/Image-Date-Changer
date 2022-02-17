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

def modify_filename(folder="asdf"):
    file_paths = os.listdir(folder)

    for file_path in file_paths:
        if file_path[0] != ".":
            print("Processing file: ", file_path)
            ext = file_path.split(".")[-1]
            fullpath = f"{folder}/{file_path}"

            epoch_time = os.path.getmtime(fullpath)
            dt = str(datetime.datetime.fromtimestamp(epoch_time)).split(' ')
            year, month, day = dt[0].split('-')
            hour, minute, second = dt[1].split(':')
            d = year + month + day
            t = hour + minute + second
            new_name = f"{folder}/vid_{d}_{t}.{ext}"

            os.rename(fullpath, new_name)




if __name__ == "__main__":
    folder = "images"
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    modify_filename(folder)
