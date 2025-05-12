import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()
sb=Scoreboard()
car = CarManager()
screen.listen()
screen.onkey(p.move, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sb.clear()
    p.increase_level()
    screen.update()
   
    car.create_cars()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(p)<20:
            game_is_on=False
        

screen.exitonclick()