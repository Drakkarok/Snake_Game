from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Yellow")
        self.penup()
        self.speed("fastest")

    def turtle_print_score(self, current_score):
        self.clear()
        self.goto(x=0, y=280)
        self.write(f"Current score: {current_score}", True, "Center", ("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", True, "Center", ("Arial", 16, "normal"))
