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
#   -- Constructs an rg.Rectangle for which:
#        -- one corner is at an rg.Point whose x and y coordinates
#             are both chose RANDOMLY from the interval 100 to 150.
#        -- the other corner is at an rg.Point whose x and y coordinates
#             are both chose RANDOMLY from the interval 160 to 200.
#             x1 = random.randrange(100, 150)
#             y1 = random.randrange(100, 150)
#             x2 = random.randrange(160, 200)
#             y2 = random.randrange(160, 200)
#             ... more code to construct the Rectangle, etc.
#
#   -- Sets the Rectangles's fill color to a color chosen RANDOMLY
#        from a LIST that the caller of the function specifies.
#        Use code like (assuming that the list is named  colors  ):
#             index = random.randrange(len(colors))
#             color = colors[index]
#             ... more code to implement the rest of this function
#
#   -- Attaches the Rectangle to a RoseWindow that the caller
#        of the function specifies.
#
#   -- Renders the RoseWindow to display the Rectangle along
#        with anything else that happens to be on the RoseWindow.
#
# The name of the function can be whatever name you choose
# (but choose a sensible name if you can).
#
########################################################################

import rosegraphics as rg
import random


def rectangle(colors, window):
    x1 = random.randrange(100, 150)
    y1 = random.randrange(100, 150)
    x2 = random.randrange(160, 200)
    y2 = random.randrange(160, 200)

    rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
    index = random.randrange(len(colors))
    color = colors[index]
    rectangle.fill_color = color
    rectangle.attach_to(window)
    window.render()
    window.continue_on_mouse_click()

    return color

