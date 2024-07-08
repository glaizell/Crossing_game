import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()



    #Detect collision

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect succesfull crossing

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_scoreboard()



screen.exitonclick()