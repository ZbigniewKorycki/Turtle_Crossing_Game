from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.1


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.starting_cars()

    def starting_cars(self):
        for car in range(10):
            car = Turtle("square")
            car.penup()
            car.goto(x=random.randrange(-300, 300), y=random.randrange(-230, 230, 60))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def create_car(self):
        chance = random.randint(1, 10)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            car.goto(x=random.randrange(300, 900), y=random.randrange(-230, 230, 60))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_distance
            car.goto(x=new_x, y=car.ycor())

    def stop_car(self):
        self.move_distance = 0

    def next_level(self):
        self.move_distance *= MOVE_INCREMENT

    def round_of_car(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.color(random.choice(COLORS))
                car.goto(x=300, y=random.randrange(-230, 230, 30))
