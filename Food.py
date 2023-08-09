from turtle import Turtle
import random

SCREEN_SIZE = [-14, 14]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.current_score = 0
        self.refresh()

    def refresh(self):
        self.goto(x=20 * random.randint(SCREEN_SIZE[0], SCREEN_SIZE[1]),
                  y=20 * random.randint(SCREEN_SIZE[0], SCREEN_SIZE[1]))

    def food_eaten(self):
        self.current_score += 1
        return self.current_score
