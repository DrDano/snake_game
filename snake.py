from turtle import Turtle, Screen


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
            new_segment.n.setposition(x=x_pos, y=0)
            x_pos -= 20
            self.segments.append(new_segment.n)

    def move(self, paces, clockwise_heading):
        screen = Screen()
        import time
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.05)
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(distance=paces)
            self.segments[0].right(angle=clockwise_heading)

