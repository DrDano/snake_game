from turtle import Turtle, Screen
import time
PACES = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_pos = -150
        for n in range(3):
            new_segment = Turtle()
            new_segment.n = Turtle(shape='square')
            new_segment.n.color('white')
            new_segment.n.penup()
            new_segment.n.goto(x=x_pos, y=0)
            x_pos -= 20
            self.segments.append(new_segment.n)

    def move(self):
        screen = Screen()
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.05)
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(PACES)
            self.segments[0].right()

