from turtle import Turtle, Screen
import random


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MIN_CAR_DISTANCE = 60
screen = Screen()
screen.register_shape("car.gif")


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            position_y = random.randint(-200, 250)
            if not self.is_position_occupied(position_y):
                car = Turtle("car.gif")  # Use the car image
                car.penup()
                car.goto(300, position_y)
                self.all_cars.append(car)

    def is_position_occupied(self, new_y):
        for car in self.all_cars:
            if abs(car.ycor() - new_y) < MIN_CAR_DISTANCE:
                return True
        return False

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



if __name__ == "__main__":
    car_manager = CarManager()


    def game_loop():
        car_manager.create_car()
        car_manager.move_cars()
        screen.ontimer(game_loop, 200)


    screen.ontimer(game_loop, 200)
    screen.mainloop()
