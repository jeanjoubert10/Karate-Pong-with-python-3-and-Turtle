# Simple pong game using Python 3 and Turtle module J Joubert 21 Oct 2019
# Sound only for mac using afplay
# winsound for windows
# This code can be copied, changed, updated and if improved - please let me know how!!


import turtle
import random
import os
#import time # and time.sleep(0.017) windows

counter = 0


def border_check():
    if ball.ycor()>290 or ball.ycor()<-290: 
        ball.dy *= -1


def p1_up():
    if p1.ycor() <= 220:
        p1.sety(p1.ycor()+60)

        
def p1_down():
    if p1.ycor() >= -220:
        p1.sety(p1.ycor()-60)


def p2_up():
    if p2.ycor() <= 220:
        p2.sety(p2.ycor()+60)


def p2_down():
    if p2.ycor() >= -220:
        p2.sety(p2.ycor()-60)


def animate_gif():
    global counter
    if p1.s == 'p1.gif' and counter%16 == 0:
        p1.s = 'p11.gif'
        p1.shape(p1.s)
    elif p1.s == 'p11.gif' and counter%18 == 0:
        p1.s = 'p1.gif'
        p1.shape(p1.s)

    if p2.s == 'p2.gif' and counter%13 == 0:
        p2.s = 'p21.gif'
        p2.shape(p2.s)
    elif p2.s == 'p21.gif' and counter%11 == 0:
        p2.s = 'p2.gif'
        p2.shape(p2.s)
        
    counter += 1
    

score_a = 0
score_b = 0

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.title('Pong')
wn.tracer(0)
wn.register_shape('p1.gif')
wn.register_shape('p1a.gif')
wn.register_shape('p2.gif')
wn.register_shape('p2a.gif')
wn.register_shape('fireball.gif')
wn.register_shape('p11.gif')
wn.register_shape('p21.gif')
#wn.register_shape('background.gif')
#wn.bgpic('background.gif')


p1 = turtle.Turtle()
p1.shape('p1.gif')
p1.color('white')
p1.shapesize(5,1)
p1.up()
p1.goto(-350,0)
p1.s = 'p1.gif'

p2 = turtle.Turtle()
p2.shape('p21.gif')
p2.color('white')
p2.shapesize(5,1)
p2.up()
p2.goto(350,0)
p2.s = 'p2.gif'

ball = turtle.Turtle()
ball.shape('fireball.gif')
ball.color('blue')
ball.up()
ball.dx = random.choice((-5, 5))
ball.dy = random.choice((-5, 5))

# Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0   PlayerB: 0", align="center", font=("Courier", 24, "normal"))

wn.listen()
wn.onkeypress(p1_up, "w")
wn.onkeypress(p1_down, 's')
wn.onkeypress(p2_up, 'Up')
wn.onkeypress(p2_down, 'Down')

game_over = False

sound_list = ['afplay p1.wav&', 'afplay p2.wav&', 'afplay p3.wav&', 'afplay p4.wav&', 'afplay p5.wav&']


while not game_over:
    wn.update()
    #time.sleep(0.017) # windows?
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    border_check()
    animate_gif()

    if ball.xcor() > 390: # Score player A
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system('afplay gong.wav&')
        ball.dx = random.choice((-5, 5))

    if ball.xcor() < -390: # Score player B
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system('afplay gong.wav&')
        ball.dx = random.choice((-5, 5))
        
    # Paddle and ball collisions
    # For the right side fist 
    if (ball.xcor() >= 340 and ball.xcor() <= 350) and ball.dx > 0 :
        if (ball.ycor() <= p2.ycor() + 60 and ball.ycor() >= p2.ycor() -60):
            ball.dx *= -1
            ball.dx -= 1
            p2.s = 'p2a.gif'
            p2.shape(p2.s)
            os.system(random.choice(sound_list))
            

    # For the left or minus side
    if (ball.xcor() <= -340 and ball.xcor() >= -350) and ball.dx < 0:
        if (ball.ycor() <= p1.ycor() + 60 and ball.ycor() >= p1.ycor() -60):
            ball.dx *= -1
            ball.dx += 1
            p1.s = 'p1a.gif'
            p1.shape(p1.s)
            os.system(random.choice(sound_list))

    # Stop if player reaches 10
    if score_a == 10 or score_b == 10:
        game_over = True

    if ball.xcor()>-200 and p1.s == 'p1a.gif':
        p1.s = 'p1.gif'
        p1.shape(p1.s)

    if ball.xcor()<200 and p2.s == 'p2a.gif':
        p2.s = 'p2.gif'
        p2.shape(p2.s)

    


    



