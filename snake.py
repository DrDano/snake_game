from turtle import Turtle, Screen
PACES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-10, 0), (-20, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
