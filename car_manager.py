from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))

    def detect_collision(self, player):
        for car in self.all_cars:
            car_left = car.xcor() - 20
            car_right = car.xcor() + 20
            car_bottom = car.ycor() - 12
            car_top = car.ycor() + 10

            player_left = player.xcor() - 10
            player_right = player.xcor() + 10
            player_top = player.ycor() + 10
            player_bottom = player.ycor() - 10

            if (car_left < player_right and car_left > player_left) or (car_right > player_left and car_right < player_right):
                if player_top > car_bottom and player_bottom < car_top:
                    return True




