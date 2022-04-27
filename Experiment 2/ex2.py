"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def Koch(t, n):
    if n < 5:
        fd(t, n)
        return
    m = n / 5.0
    Koch(t, m)
    t.lt()
    Koch(t, m)
    t.rt()
    Koch(t, m)
    t.rt()
    Koch(t, m)
    t.lt()
    Koch(t, m)


def Koch_figure(t, n):
    for i in range(4):
        Koch(t, n)
        t.rt()


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -60
bob.y = 90
bob.redraw()

Koch_figure(bob, 600)

world.mainloop()
