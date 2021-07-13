from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(n=0)

ted = Turtle()
segments = []
game_is_on = True
turtle_num = 0
x_pos = -100
for n in range(3):
    ted.n = Turtle(shape='square')
    print(ted.n)
    ted.n.color('white')
    ted.n.penup()
    pos = ted.n.setposition(x=x_pos, y=0)
    x_pos -= 20
    segments.append(ted.n)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()
