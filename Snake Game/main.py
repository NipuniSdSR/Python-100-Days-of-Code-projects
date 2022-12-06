from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.listen()

game_is_on = True

while game_is_on:
    screen.update()  # refresh the screen
    time.sleep(0.2)  # delay 1s next command AFTER REFRESH

    snake.move()

    # Detect collision with food : distance() function can compare distance of two turtle instances
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.set_high_score()
        snake.reset_snake()

    # Detect snake collision with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.set_high_score()
            snake.reset_snake()
    # if head collide with any segment in the tail:
    #       Trigger the game over

screen.exitonclick()
