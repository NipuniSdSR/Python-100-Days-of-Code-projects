import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move()

    # Collisions with cars
    for car in cars.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing

    if player.is_at_finish_line():
        scoreboard.increase_level()
        cars.speed_up_cars()
        player.go_to_start()


screen.exitonclick()