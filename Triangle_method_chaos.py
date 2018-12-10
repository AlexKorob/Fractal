# work time: ~20-25s
from turtle import sety, setx, penup, pendown, left, right, forward, dot, \
                tracer, done, towards, distance, speed, setup
from random import randint, choice
from time import time


def choose_random():
    # 0 left - attract
    # 1 top - attract
    # 2 right - attract
    dots = [0, 1, 2]
    return choice(dots)


def start_dot():
    penup()
    start_x = randint(-300, 300)
    start_y = randint(-150, 150)
    setx(start_x)
    sety(start_y)
    pendown()
    dot(2)


def create_attractes():
    global attractes

    for i in pos_attractes:
        penup()
        setx(i[0])
        sety(i[1])
        pendown()
        dot(2)


start_time = time()
pos_attractes = [(-300, -300), (0, 300), (300, -300)]

setup(1080, 700)
tracer(0)
speed(0)
create_attractes()
start_dot()

for i in range(30000):
    dot_to_attracte = pos_attractes[choose_random()]
    # rotate turtle to attract
    angle_to_rotate = towards(dot_to_attracte)
    left(angle_to_rotate)
    dist = distance(dot_to_attracte)
    penup()
    forward(dist/2)
    pendown()
    dot(2)
    right(angle_to_rotate)

done()
