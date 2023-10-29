import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    car_manager.round_of_car()

    if player.reset():
        scoreboard.update_level()
        car_manager.next_level()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            car_manager.stop_car()
            game_is_on = False


screen.exitonclick()
