"""Memory, puzzle game of number pairs.

Exercises
1. Count and print how many taps occur. # DONE
2. Decrease the number of tiles to a 4x4 grid. # DONE
3. Detect when all tiles are revealed. # FIX
4. Center single-digit tile. # TODO
5. Use letters instead of tiles. # DONE
"""

from random import *
from turtle import *

from freegames import path

letters = ['a', 'b', 'c' , 'd', 'e', 'f', 'g', 'h']
car = path('car.gif')
tiles = letters * 2
state = {'mark': None}
hide = [True] * 16
clicks = 0

def click(x, y):
    """Count how many taps occur."""
    global clicks
    clicks += 1 

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def play(x, y):
    click(x, y)
    tap(x, y)

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+40, y+25) #Center here
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    up()
    goto(-190, 170)
    color('black')
    write(f'Taps: {clicks}', font = ('Arial', 12))     

    update()

    if not any(hide):
        goto(0, 0)
        write("You win!", align='center', font=('Arial', 30, 'normal'))
        return

    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(play)
draw()
done()
