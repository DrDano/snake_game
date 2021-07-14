from snake import Screen, Snake

screen = Screen()
screen.tracer(n=0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()
snake.move()

screen.exitonclick()
