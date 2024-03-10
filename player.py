from turtle import Turtle


class Player():
    def __init__(self):
        self.player = Turtle(shape="turtle")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(0,-280)

    def go_up(self):
        self.player.sety(self.player.ycor()+20)
    def go_down(self):
        self.player.sety(self.player.ycor()-20)
