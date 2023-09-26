from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # print("NO NOM NOm")
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect Collision with tail means if head collides with any segment in tha tail.
    for segm in snake.segments[1:]:
        # if segm == snake.head:
        #     pass
        if snake.head.distance(segm) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()
