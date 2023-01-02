from turtle import Screen
import time
from snake import Snake
from score import Scoreboard
from food import Food


screen = Screen()
screen.bgcolor("black")
screen.title("My snake game")
screen.setup(600,600)
screen.tracer(0)

#instantiate snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()


    #detect collision withe food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.gameover()

    #detect collision with tail.
    for segment in Snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()







screen.exitonclick()