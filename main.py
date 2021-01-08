from turtle import Screen, Turtle
import time
import snake
screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
snake = snake.Snake()

is_game_on = True

snake.creat_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)


    snake.move()















screen.exitonclick()