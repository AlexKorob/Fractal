from turtle import *


def draw(where, line):
    global pos_current, pos_next

    def move_n_add():
        fillcolor('#fff')
        begin_fill()
        list_turn = [60, 120, 120, 60]
        for i in range(len(list_turn)):
            right(list_turn[i])
            if i == 3:
                break
            forward(line/2)
            pos_next.append(position())
            forward(line/2)
        end_fill()

    penup()
    pos_turtle_x, pos_turtle_y = pos_current.pop(0)
    setx(pos_turtle_x)
    sety(pos_turtle_y)

    if where == 'bottom':
        pendown()
        move_n_add()

    elif where == 'right':
        left(60)
        forward(line)
        right(60)
        pendown()
        move_n_add()

    elif where == 'left':
        left(120)
        forward(line)
        right(120)
        pendown()
        move_n_add()


pos_current = []
pos_next = []
line = 500
speed(0)

# create main big triangle
fillcolor('#000')
penup()
setup(1080, 720)
sety(200)
setx(-200)
pendown()
begin_fill()
forward(line)
right(120)
forward(line)
right(120)
forward(line)
end_fill()
backward(line/2)
right(120)

# create one inside triangle
pos_current.append(position())
draw('right', line/2)

# main
num_iter = 0

while num_iter != 7:
    line /= 2
    length_pos_current = int(len(pos_current)/3)
    for i in range(length_pos_current):
        draw('right', line)
        draw('bottom', line)
        draw('left', line)
    pos_current = pos_next
    post_next = []
    num_iter += 1

hideturtle()
done()
