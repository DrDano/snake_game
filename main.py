from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

from snake import SnakeMovement
tom = SnakeMovement()


screen.exitonclick()
