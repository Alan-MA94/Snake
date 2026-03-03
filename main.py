from turtle import Screen
from snake import Snake, Walls
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=950, height=950)
screen.bgcolor("black")
screen.title("El me zógo del Bisso")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
walls = Walls()

screen.listen()
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")

gaming = True
while gaming:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.scoreboard()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()    
        snake.extend()
    
    # detect collision with wall.
    wall_a = snake.head.xcor() < -450
    wall_b = snake.head.xcor() > 450
    wall_c = snake.head.ycor() < -340
    wall_d = snake.head.ycor() > 340
    
    # detect end game 
    if wall_a or wall_b or wall_c or wall_d:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail. 
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()            
            snake.reset()
     

screen.exitonclick()