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
# To solve this problem, you will write code in this module (m3)
# as well as in modules m4 and m5, as follows:
#
# 1. In this module (m3), write code that will:
#      a. Ask the user (on the console) to enter a color.  For example:
#           in one run of this program the user might enter
#            Construct and display an rg.RoseWindow.
#      b. Call a function
#                DEFINED IN ** m4 **
#         that, when called:
#           -- Constructs an rg.Circle whose radius is chosen RANDOMLY
#                from the interval 20 to 70 and whose center is an
#                rg.Point whose x and y coordinates are both chosen
#                RANDOMLY from the interval 50 to 150.  Use code like:
#                   r = random.randrange(20, 70)
#                   x = random.randrange(50, 150)
#                   y = random.randrange(50, 150)
#                    ... more code to construct the Circle, etc.
#           -- Sets the Circle's fill color to whatever color the
#                user entered via code in this module (m3).
#           -- Attaches the Circle to the RoseWindow constructed
#                via code in this module (m3).
#           -- Renders the RoseWindow to display the Circle along
#              with anything else that happens to be on the RoseWindow.
#      c. Call a function
#                DEFINED IN ** m5 **
#         that, when called:
#           -- Constructs an rg.Rectangle whose corners are at
#                rg.Points whose x and y coordinates are both chosen
#                RANDOMLY from the interval 100 to 200.  Use code like:
#                   x1 = random.randrange(100, 200)
#                   y1 = random.randrange(100, 200)
#                   x2 = random.randrange(100, 200)
#                   y2 = random.randrange(100, 200)
#                    ... more code to construct the Rectangle, etc.
#           -- Sets the Rectangle's fill color to whatever color the
#                user entered via code in this module (m3).
#           -- Attaches the Rectangle to the RoseWindow constructed
#                via code in this module (m3).
#           -- Renders the RoseWindow to display the Rectangle along
#              with anything else that happens to be on the RoseWindow.
#      d. Call
#
# IMPORTANT:
#
########################################################################

import rosegraphics as rg
import m4
import m5


def main():
    """ See above for what this function should accomplish. """
    color1 = input('Enter a color: ')
    color2 = input('Enter a color: ')
    color3 = input('Enter a color: ')

    window = rg.RoseWindow()
    m4.circle(color1, window)
    color = m5.rectangle([color2, color3], window)

    m4.circle(color, window)

    for _ in range(5):
        m5.rectangle([color1, color2, color3], window)

    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
