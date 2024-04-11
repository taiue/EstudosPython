from fileinput import filename
import random

feet_in_mile = 5280
meter_in_kilometer = 1000
letters = ["A", "B", "C"]

def get_file_ext():
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)


