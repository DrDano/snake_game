from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

ted = Turtle()
turtle_num = 0
for turtle_name in range(3):
    print(turtle_name)

screen.exitonclick()
