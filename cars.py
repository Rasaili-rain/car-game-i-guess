from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "lime", "green",
        "cyan", "blue", "purple", "pink", "magenta"]
NO_OF_CARS = 10


class Cars():
    def __init__(self):
        self.car_list = []

    def create_cars(self):
        for i in range(NO_OF_CARS+1):
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-12, 12)*20
            x_pos = random.randint(10, 50)*20
            new_car.goto(x_pos, y_pos)
            self.car_list.append(new_car)

    def move_cars(self,player_postion):
        for car in self.car_list:
            if car.xcor() > -500:
                car.setx(car.xcor()-10)
                if car.distance(player_postion) <= 20:
                    return True

            else:
                car.color(random.choice(COLORS))
                car.goto(random.randint(10, 50)*20, random.randint(-15, 15)*20)
