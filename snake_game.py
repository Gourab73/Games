import turtle
import random
import time

delay = 0.1

s = turtle.Screen()
s.setup(900,700)
s.title("Snake Game")
s.bgcolor("black")
s.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

food = turtle.Turtle()
food.shape("square")
food.color("red")
xcor = random.randint(-290,290)
ycor = random.randint(-290,290)
food.penup()
food.goto(xcor,ycor)
food.speed(0)

score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Score: 0   ", align="center", font=("Courier",24,"normal"))

Score = 0


def move_right():
    snake.direction = "right"
def move_left():
    snake.direction = "left"
def move_up():
    snake.direction = "up"
def move_down():
    snake.direction = "down"

def moving():
    if snake.direction == "right":
        snake.setx(snake.xcor()+20)
    elif snake.direction == "left":
        snake.setx(snake.xcor()-20)
    elif snake.direction == "up":
        snake.sety(snake.ycor()+20)
    elif snake.direction == "down":
        snake.sety(snake.ycor()-20)

s.listen()
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")

body_segments = []

while True:
    s.update()

    if snake.distance(food) < 20:
        xcor = random.randint(-290, 290)
        ycor = random.randint(-290, 290)
        food.goto(xcor,ycor)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        body_segments.append(new_segment)

        Score += 1
        score.clear()
        score.write("Your Score: {} ".format(Score), align="center", font=("Courier", 24, "normal"))

    for i in range(len(body_segments)-1, 0, -1):
        body_segments[i].goto(body_segments[i-1].xcor(), body_segments[i-1].ycor())

    #move segment 0 where the head is
    if len(body_segments) > 0:
        body_segments[0].goto(snake.xcor(), snake.ycor())

    if snake.xcor() > 430 or snake.xcor() < -430 or snake.ycor() > 330 or snake.ycor() < -330:
        time.sleep(0.1)
        snake.direction = "Stop"
        snake.hideturtle()
        food.hideturtle()
        score.penup()
        score.goto(0, 20)
        score.color("red")
        score.write("GAME OVER!!!", align="center", font=("Courier", 24, "normal"))


    moving()

    for new_segment in body_segments:
        if new_segment.distance(snake) < 20:
            time.sleep(0.1)
            snake.direction = "Stop"
            snake.hideturtle()
            food.hideturtle()
            score.penup()
            score.goto(0, 20)
            score.color("red")
            score.write("GAME OVER!!!", align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

s.mainloop()