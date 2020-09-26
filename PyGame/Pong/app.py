import turtle as turt
import os
import winsound
from sys import platform

# Check OS
if platform == "linux" or platform == "linux2":
    def playit():
        os.system("aplay bounce.wav&")
elif platform == "darwin":
    def playit():
        os.system("afplay bounce.wav&")
elif platform == "win32":
    def playit():
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

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

# Score
home = 0
visitor = 0

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
ball.dx = 0.15
ball.dy = 0.15


# Pen (Turtle 🐢)
pen = turt.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("🏡Home🏡: 0     ⛩Visitor🧭: 0", align="center", font=("Russo One", 24, "normal"))

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
         playit()
    if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy = ball.dy * -1
         playit()
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        home = home + 1
        pen.clear()
        pen.write("🏡Home🏡: {}     ⛩Visitor🧭: {}".format(home, visitor), align="center", font=("Russo One", 24, "normal"))
        playit()
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        visitor = visitor + 1
        pen.clear()
        pen.write("🏡Home🏡: {}     ⛩Visitor🧭: {}".format(home, visitor), align="center", font=("Russo One", 24, "normal"))
        playit()

    # Ball and Paddle Coliision
    if (ball.xcor() > 340 and ball.xcor() < 350 and(ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() -40)):
        ball.setx(340)
        ball.dx = ball.dx * -1
        playit()

    if (ball.xcor() < -340 and ball.xcor() > -350 and(ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() -40)):
        ball.setx(-340)
        ball.dx = ball.dx * -1
        playit()
