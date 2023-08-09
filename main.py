from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

is_game_on = True
current_score = 0

snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

score_board.turtle_print_score(current_score)

while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        current_score = food.food_eaten()
        score_board.turtle_print_score(current_score)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score_board.game_over()
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         score_board.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()



####################
screen.exitonclick()
