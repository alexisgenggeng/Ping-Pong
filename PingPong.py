import turtle

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(5, 1)
paddleA.penup()
paddleA.goto(-350, 0)

#paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(5, 1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=1
ball.dy=1

#scoreboard
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score
scoreA=0
scoreB=0

def paddleA_up():
    y=paddleA.ycor()
    y +=40
    paddleA.sety(y)

def paddleA_down():
    y=paddleA.ycor()
    y -=40
    paddleA.sety(y)
#B
def paddleB_up():
    y=paddleB.ycor()
    y +=40
    paddleB.sety(y)

def paddleB_down():
    y=paddleB.ycor()
    y -=40
    paddleB.sety(y)

#keys
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

#game loop
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boarder checking
    #top and bottom
    if ball.ycor()>290:
        ball.dy *=-1
    elif ball.ycor()<-290:
        ball.dy *=-1

    #left and right
    if ball.xcor()>350:
        ball.dx *=-1
        scoreA+=1
        board.clear()
        board.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    elif ball.xcor()<-350:
        ball.dx *=-1
        scoreB+=1
        board.clear()
        board.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    #return
    if ball.xcor()<-340 and ball.ycor()<paddleA.ycor()+50 and ball.ycor()>paddleA.ycor()-50:
        ball.dx *=-1

    elif ball.xcor()> 340 and ball.ycor()<paddleB.ycor()+50 and ball.ycor()>paddleB.ycor()-50:
        ball.dx *=-1
