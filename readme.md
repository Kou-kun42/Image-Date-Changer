# Image Date Changer

### Overview

This is a simple date changer that updates image metadata inside a specified folder. I created this to correct the creation/modified dates on images after that were downloaded from google photos. By default the dates will show when the file was downloaded, not the date that the picture was taken. This script updates the modified date with the EXIF data stored in the image file. On mac this also changes the creation date. Updating the creation/modified date makes it much easier to sort the images in a file browser and allows you to view them in a more organized manner.

### Get Started

To get started, first clone this repo:

```
git clone https://github.com/Kou-kun42/Image-Date-Changer.git
```

Then copy your images into a folder (by default "images" in the root of the repo). It's always important to copy them or have a backup before running the script in case of any accidents.

Next, set up a virtual environment:

```
python3 -m venv env
```

Activate it:

```
source env/bin/activate
```

Then install dependencies:

```
pip3 install -r requirements.txt
```

Finally, run the script:

```
python3 date_changer.py
```

If your images are in another folder:

```
python3 date_changer.py "/path/to/images"
```
