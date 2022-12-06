from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings.

r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

ball = Ball()

scoreboard = Scoreboard()

# to listen to the keypress
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(ball.move_speed)

    ball.move()

    # Detect the collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce back y
        ball.bounce_y()

    # Detect collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
