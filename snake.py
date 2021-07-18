from turtle import Turtle, Screen
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
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(PACES)

    def up(self):
        self.segments[0].setheading(to_angle=90)

    def down(self):
        self.segments[0].setheading(to_angle=270)

    def left(self):
        self.segments[0].setheading(to_angle=180)

    def right(self):
        self.segments[0].setheading(to_angle=0)
