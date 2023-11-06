"""CQ07 - Intro to Object Oriented Programming."""
__author__ = "730679279"
from lessons.CQ07.point import Point

new_point = Point(1.2, 1.4)
new_point.scale_by(new_point, 2)
new_point.scale(new_point, 3)