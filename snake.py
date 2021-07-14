
class SnakeMovement:

    def __init__(self, paces, clockwise_heading, segs):
        from turtle import Turtle, Screen
        import time
        ted = Turtle()
        screen = Screen()
        screen.tracer(n=0)
        segments = []
        game_is_on = True
        x_pos = -100

        for n in range(0, segs):
            ted.n = Turtle(shape='square')
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
            segments[0].forward(distance=paces)
            segments[0].right(angle=clockwise_heading)

