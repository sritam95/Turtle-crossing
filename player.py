STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from car_manager import CarManager
from turtle import Turtle
from scoreboard import Scoreboard
sb=Scoreboard()
car=CarManager()
class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        
    def move(self):
        newy=self.ycor()+MOVE_DISTANCE
        self.goto(0,newy)
        
    def increase_level(self):
        if self.ycor()>=FINISH_LINE_Y:
            sb.increse()
            self.goto(STARTING_POSITION)
            car.increase_speed()
            
        
        
