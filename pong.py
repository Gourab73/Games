import turtle

s = turtle.Screen()
s.title("Pong")
s.bgcolor("black")
s.setup(800,600)
s.tracer(0)


#paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.speed(0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.speed(0)

#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 2   #ball's movement changes by 2px
ball.dy = 2

#pen
score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: 0   Player B: 0 ", align="center", font=("Courier",24,"normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

s.listen()
s.onkeypress(paddle_a_up, "u")
s.onkeypress(paddle_a_down, "d")
s.onkeypress(paddle_b_up, "Up")
s.onkeypress(paddle_b_down, "Down")

score_a = 0
score_b = 0

# main game loop
while True:
    s.update()

    #movement of the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border occurrences
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}   Player B: {} ".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}   Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #collision with paddles
    """if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b - 50:

        ball.dx *= -1
    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a - 50:

        ball.dx *= -1"""
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1