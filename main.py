from snake import Screen, Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(n=0)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)


game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    # detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 \
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    # If the head collides with any segment in the tail:
        # trigger game_over
    # for segment in snake.segments:
    #     if segment == snake.segments[0]:
    #         pass
    #     elif snake.segments[0].distance(segment) > 10:
    #         game_is_on = False
    #         scoreboard.game_over()

screen.exitonclick()
