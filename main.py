import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.up_move, "Up")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for carx in car.all_cars:
        if carx.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_the_end():
        player.go_to_start()
        car.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
