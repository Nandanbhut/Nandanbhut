# Creating a pong game with the turtle module
# Coding portion 

import turtle 

win = turtle.Screen()
win.title("pong by nandan")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)  # This makes our game faster by not auto updating the game 

# Score 
score_a = 0 
score_b = 0

# Paddle A
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.22
ball.dy = 0.22

# Pen module    
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  |  Player B: 0", align="center", font=("Courier", 16, "normal"))


# Function for paddle A
def paddle_up(): 
    up = paddle.ycor()
    up += 20
    paddle.sety(up)

def paddle_down(): 
    down = paddle.ycor()
    down -= 20
    paddle.sety(down)

# Function for paddle B
def paddle_b_up(): 
    up = paddle_b.ycor()
    up += 20
    paddle_b.sety(up)

def paddle_b_down(): 
    down = paddle_b.ycor()
    down -= 20
    paddle_b.sety(down)

# Keyinputs 
win.listen()
win.onkeypress(paddle_up, "w")
win.onkeypress(paddle_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main game loop for updating 
while True: 
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  |  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1 
        pen.clear()
        pen.write ("Player A: {}  |  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    # Paddle and ball collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle.ycor() + 40 and ball.ycor() > paddle.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1        

    # Ending the game 
    if score_a == 3: 
        break 
    if score_b == 3: 
        break 
        

# The game ends without calling out who wins
