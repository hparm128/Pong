import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

y_position = -330
for num in range(25):
    line = Turtle("square")
    line.speed("fastest")
    line.penup()
    line.turtlesize(stretch_len=0.2)
    line.color("white")
    line.goto(0, y_position)
    y_position += 30

screen.listen()
screen.onkeypress(key="Up", fun=player1.up)
screen.onkeypress(key="Down", fun=player1.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Move player 2 to hit ball
    while ball.ycor() > player2.ycor():
        player2.up()
    while ball.ycor() < player2.ycor():
        player2.down()

    # Detect collision paddles
    if ball.xcor() > 320 and ball.distance(player1) < 50:
        ball.hit_paddle()
    elif ball.xcor() < -320 and ball.distance(player2) < 50:
        ball.hit_paddle()

    # Detect collision with left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.user_point()
    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.computer_point()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
