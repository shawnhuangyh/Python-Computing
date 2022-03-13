import math
from swampy.TurtleWorld import *

def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle / 2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle / 2)

def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def semicircle(t, r):
    """"
    画半圆
    """
    arc(t, r, 180)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

# 初始化设置
def init():
    world = TurtleWorld()
    simon = Turtle()
    simon.set_pen_color('#FF9900')
    simon.delay = 1e-8
    return world, simon

# 流汗黄豆
def emoji():
    # 脸
    radius1 = 60
    simon.pu()
    simon.fd(radius1)
    simon.lt()
    simon.pd()
    circle(simon, radius1)

    # 嘴
    simon.set_pen_color('#CC6633')
    radius2 = 50
    arc1 = 15
    simon.pu()
    simon.lt()
    simon.fd(radius1 - radius2)
    simon.lt()
    simon.pd()
    arc(simon, radius2, -180)
    simon.rt()
    simon.fd(radius2 * 2)
    simon.rt()
    simon.pu()
    arc(simon, radius2, -arc1)
    simon.rt(-arc1 + 90)
    simon.pd()
    simon.fd(2 * radius2 * math.cos(arc1 / 180 * math.pi))
    simon.pu()
    simon.rt(-arc1 + 90)
    arc(simon, radius2, -arc1)
    simon.rt()
    simon.fd(30)

    # 眼
    k = radius2 / 5 * 2
    radius3 = 15
    simon.lt()
    simon.fd(18)
    simon.rt()
    simon.fd(radius3)
    simon.lt()
    simon.pd()
    semicircle(simon, radius3)
    simon.lt(120)
    arc(simon, 30, -60)
    simon.pu()
    arc(simon, 30, -300)
    simon.rt(120)

    simon.lt()
    simon.fd(radius3 * 2 + k * 3 - 20)
    simon.lt()
    simon.pd()
    semicircle(simon, radius3)
    simon.lt(120)
    arc(simon, 30, -60)
    simon.pu()
    arc(simon, 30, -300)
    simon.rt(120)

    # 汗
    simon.set_pen_color('#0099FF')
    simon.lt()
    simon.fd(30)
    simon.lt()
    simon.fd(40)

    arc2 = 15
    radius4 = 40
    simon.lt(180 - arc2)
    simon.pd()
    simon.fd(radius4)
    simon.lt(arc2)
    semicircle(simon, radius4 * math.sin(math.pi * arc2 / 180))
    simon.lt(arc2)
    simon.fd(radius4)

    # 爬
    simon.pu()
    simon.fd(2000)

if __name__ == '__main__':
    world, simon = init()
    emoji()
    wait_for_user()
