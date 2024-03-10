from turtle import Turtle,Screen
import time
from cars import Cars
from player import Player
from scoreboard import Scoreboard

FINISH_LINE =  280
speed = 0.05

screen = Screen()
screen.setup(height=600,width=800)
screen.tracer(0)

cars = Cars()
player = Player()
scoreboard = Scoreboard()


cars.create_cars()

game_is_on = True
screen.listen()
screen.onkeypress(player.go_up,"Up")
screen.onkeypress(player.go_down,"Down")

while game_is_on:
    time.sleep(0.2)
    screen.update()
    if cars.move_cars(player.player.position()) == True:
        game_is_on = False
        screen.clear()
        scoreboard.game_over()
    if player.player.ycor() >= FINISH_LINE:
        player.player.goto(0,-280)
        speed *= 0.5
        scoreboard.update_score()

screen.exitonclick()
