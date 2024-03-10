from turtle import Turtle
ALIGNMENT ="center"
FONT = ('Courier', 16, 'normal')
class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0,270)
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.goto(0,280)
        self.write(f"current score ={self.score}",align=ALIGNMENT,font=FONT)
        self.score += 1
