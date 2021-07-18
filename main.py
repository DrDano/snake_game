from snake import Screen, Snake
import time

screen = Screen()
screen.tracer(n=0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

snake.move()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
