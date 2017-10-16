"""
PRACTICE Test 3.

This problem provides practice at:
  ***  Using multiple modules to solve a problem.  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.  October 2016.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# To solve this problem, you will write code in modules m3, m4 and m5.
#
# In this module (m4), define a function that, when called:
#
#   -- Constructs an rg.Circle whose radius is chosen RANDOMLY
#        from the interval 20 to 70 and whose center is an
#        rg.Point whose x and y coordinates are both chosen
#        RANDOMLY from the interval 50 to 150.  Use code like:
#              r = random.randrange(20, 70)
#              x = random.randrange(50, 150)
#              y = random.randrange(50, 150)
#              ... more code to construct the Circle, etc.
#
#   -- Sets the Circle's fill color to a color that the caller
#        of the function specifies.
#
#   -- Attaches the Circle to a RoseWindow that the caller
#        of the function specifies.
#
#   -- Renders the RoseWindow to display the Circle along
#        with anything else that happens to be on the RoseWindow.
#
# The name of the function can be whatever name you choose
# (but choose a sensible name if you can).
#
########################################################################

import rosegraphics as rg
import random


def circle(color, window):
    r = random.randrange(20, 70)
    x = random.randrange(50, 150)
    y = random.randrange(50, 150)
    circle = rg.Circle(rg.Point(x, y), r)
    circle.fill_color = color
    circle.attach_to(window)
    window.render()
    window.continue_on_mouse_click()

