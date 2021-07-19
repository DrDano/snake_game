from turtle import Turtle, Screen
PACES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_pos = -50
        for n in range(3):
            new_segment = Turtle()
            new_segment.n = Turtle(shape='square')
            new_segment.n.color('white')
            new_segment.n.penup()
            new_segment.n.goto(x=x_pos, y=0)
            x_pos -= 20
            self.segments.append(new_segment.n)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(PACES)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(to_angle=UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(to_angle=DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(to_angle=LEFT)

    def right(self):
        if self.segments[0] != LEFT:
            self.segments[0].setheading(to_angle=RIGHT)
