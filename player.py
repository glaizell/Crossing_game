from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DISTANCE_UP = 10
MOVE_DISTANCE_DOWN = -10

FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("red")
        self.penup()
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE_UP)

    def move_down(self):
        self.forward(MOVE_DISTANCE_DOWN)

    def go_to_start(self):
        self.goto(STARTING_POS)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


