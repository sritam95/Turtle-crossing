COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speeding= STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_r= random.randint(1,6)
        if random_r == 1:
            new_box = Turtle()
            new_box.shape("square")
            new_box.shapesize(stretch_len=2, stretch_wid=1)
            new_box.penup()
            new_box.color(random.choice(COLORS))
            newy=random.randint(-250, 250)
            new_box.goto(300, newy)
            self.all_cars.append(new_box)
        
    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.speeding)
            
    def increase_speed(self):
        self.speeding+=MOVE_INCREMENT
        
        
        
    
