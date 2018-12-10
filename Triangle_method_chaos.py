from turtle import *
from random import randint, choice


def choose_random():
    dots = [0,1,2]
    return choice(dots)

def start_dot():
    penup()
    start_x = randint(-300, 300)
    start_y = randint(-150, 150)
    setx(start_x)
    sety(start_y)
    pendown()
    dot(5)


def create_attractes():
    global attractes

    for i in pos_attractes:
        penup()
        setx(i[0])
        sety(i[1])
        pendown()
        dot(5)

# 0 left - attract
# 1 top - attract
# 2 right - attract
pos_attractes = [(-300, -300), (0, 300), (300, -300)]

setup(1080, 700)
speed(0)
create_attractes()
start_dot()

for i in range(1):
    dot_to_attracte = pos_attractes[choose_random()]
    #rotate turtle to attract
    t = towards(dot_to_attracte)
    print(dot_to_attracte)
    print(t)
    left(t)
    dist = distance(dot_to_attracte)
    
    
done()
