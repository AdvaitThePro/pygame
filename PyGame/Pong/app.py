import turtle as turt

#create window
win = turt.Screen()
#window title
win.title("Pong 🏓")
#set BG colur to my favourite!
win.bgcolor("#0066ff")
# set it up
win.setup(width=800, height=600)
# no autoupdates
win.tracer(0)

# Paddle A
player_1 = turt.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("#ff3300")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

# Paddle B
player_2 = turt.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("#ff3300")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

# Ball 🎱
ball = turt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Lime")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Functions
def player_1_up():
    y = player_1.ycor()
    y = y + 20
    player_1.sety(y)
def player_1_down():
    y = player_1.ycor()
    y = y - 20
    player_1.sety(y)
def player_2_up():
    y = player_2.ycor()
    y = y + 20
    player_2.sety(y)
def player_2_down():
    y = player_2.ycor()
    y = y - 20
    player_2.sety(y)

# Keyboard Binding
win.listen()
win.onkeypress(player_1_up, "w")
win.onkeypress(player_1_down, "s")
win.onkeypress(player_2_up, "Up")
win.onkeypress(player_2_down, "Down")

# main game loop
while True:
    win.update()

    #  Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
         ball.sety(290)
         ball.dy = ball.dy * -1
    if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy = ball.dy * -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
    if ball.xcor() < -390:
       ball.goto(0, 0)
       ball.dx = ball.dx * -1

