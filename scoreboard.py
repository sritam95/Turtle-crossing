FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.level=1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",font=FONT)
    def increse(self):
        self.level+=1
        self.update_score()
        
        
    
