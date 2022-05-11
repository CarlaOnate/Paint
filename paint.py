"""
GAME: Paint.
AUTHOR 1: Carla Onate Gardella.
AUTHOR 2: Octavio Augusto Aleman Esparza.

DATE: May - 10 - 2022.

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def drawCircle(start, end):
    #Draws circle with custom radius
    up()
    goto(start.x, start.y)
    radius = abs(start.x - end.x) # radius calculated from start and end of x axis
    down()
    begin_fill() # We want the circle to be filled after it's created
    circle(radius) # Creates the circle with specific radius
    end_fill()

def rectangle(start, end): # rectangle() function has been completed. It draws a rectangle with a custom base lenght.
    "Draw rectangle from start to end." 
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2): # The cycle has two iterations, so that the base line and left side are drawn in the first one, and top line and right side in the second one.
        forward(end.x - start.x) # The base line (and top line in the second iteration) of the rectangle is drawn.
        left(90) # The pen is rotated at an angle of 90° to the left.
        forward((end.x - start.x) * 0.5) # The side lines are drawn with a lenght equal to half the lenght of the base line.
        left(90) # The pen is rotated at an angle of 90° to the left.

    end_fill()

def triangle(start, end): # The triangle() function has been completed. It draws an equilateral triangle with custom sides length.
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3): # The cycle has 3 iterations, each one will draw a side from the triangle, starting with the base line and then going left to right.
        forward(end.x - start.x) # The sides are drawn with a custom length. 
        left(120) # The pen is rotated at an angle of 120° to the left.

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
# If user clicks on O the all the lines or shapes will be orange
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', drawCircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
listen()
done()