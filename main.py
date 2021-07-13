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
    for seg in segments:
        seg.forward(15)

screen.exitonclick()
