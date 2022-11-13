from collections.abc import Iterable
import re


def ang2rad(angle):
    angle, minute, second = re.findall("(\d+)°(\d+)?'?(\d+)?",angle)[0]
    if minute == '':
        minute = 0
    if second == '':
        second = 0
    angle = int(angle) + int(minute)/60 + int(second)/60/60
def convert_to_rad(angle):
    if isinstance(angle, Iterable):
        rad_list = []
        for angle_ in angle:
            rad_list.append(ang2rad(angle_))
        return rad_list
    else:
        return ang2rad(angle)