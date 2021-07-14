from turtle import Screen
from snake import Snake
from time import time

screen = Screen()
screen.tracer(n=0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()

screen = Screen()
screen.exitonclick()
