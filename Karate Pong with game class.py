# Simple Karate Pong playing with gif files, gif animation and wav sound files
# Jean Joubert 21 Nov 2019
# afplay for mac (winsound for windows)
# written on mac osX - may need speed adjustment on windows

# Game class makes start/game over screen/new game easy to manage
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
import random
import os
#import time # and time.sleep(0.017) windows??

 
class Paddle(turtle.Turtle):
    def __init__(self,xpos, s):
        super().__init__(shape='square')
        self.xpos = xpos
        self.shapesize(5, 1)
        self.color('white')
        self.up()
        self.s = s
        self.shape(self.s)
        self.goto(self.xpos, 0)
        

    def move_up(self):
        if self.ycor() <= 220:
            self.sety(self.ycor()+50)


    def move_down(self):
        if self.ycor()>= -220:
            self.sety(self.ycor()-50)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='fireball.gif')
        self.up()
        self.color('blue')
        self.dx = random.choice((-5,5))
        self.dy = random.choice((-5,5))

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        if self.ycor() <= -280 or self.ycor() >= 280:
            self.dy *= -1


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('red')
        self.up()
        self.hideturtle()
         

class Game():
    def __init__(self):
        # Initialize the screen and setup
        self.win = turtle.Screen()
        self.win.setup(800,600)
        self.win.bgcolor('white')
        self.win.title('Karate Pong using python 3 and turtle')
        self.win.tracer(0)
        self.win.listen()
        self.running = True
        
        self.sound_list = ['afplay p1.wav&', 'afplay p2.wav&', 'afplay p3.wav&', 'afplay p4.wav&', 'afplay p5.wav&']

        self.shape_list = ['p1.gif', 'p11.gif', 'p2.gif', 'p21.gif', 'p1a.gif', 'p2a.gif', 'fireball.gif']
        for shape in self.shape_list:
            self.win.register_shape(shape)

        self.pen = Scoreboard()

    def new(self):
        # Start a new game after start screen/game over screen
        self.win.bgcolor('white')
        self.paddle1 = Paddle(-350, 'p1.gif')
        self.paddle2 = Paddle(350, 'p2.gif')
        self.ball = Ball()
        
        self.score1 = 0
        self.score2 = 0
        self.counter = 0

        self.pen.clear()
        self.pen.goto(0,260)
        self.pen.write("PlayerA: 0   PlayerB: 0", align="center", font=("Courier", 24, "normal"))

        self.run()

    def run(self):
        # Run the events (key presses), updates and gif animations
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.animate_gif()
           

    def events(self):
        self.win.onkey(self.paddle1.move_up, 'w')
        self.win.onkey(self.paddle1.move_down, 's')
        self.win.onkey(self.paddle2.move_up, 'Up')
        self.win.onkey(self.paddle2.move_down,'Down')

    
    def update(self):
        self.win.update()
        #time.sleep(0.017) # windows??
        
        self.ball.move()

        # Paddle 1 check:
        if (self.paddle1.xcor() <= self.ball.xcor()-10 <= self.paddle1.xcor()+10) and self.ball.dx < 0:
            if self.paddle1.ycor()-60 <= self.ball.ycor() <= self.paddle1.ycor()+60:
                self.ball.dx *= -1
                self.ball.dx += 1  # Speed up the ball
                self.paddle1.s = 'p1a.gif'
                self.paddle1.shape(self.paddle1.s)
                os.system(random.choice(self.sound_list))
                

        # Paddle 2 check:
        if (self.paddle2.xcor()-10 <= self.ball.xcor() <= self.paddle2.xcor()) and self.ball.dx > 0:
            if self.paddle2.ycor()-60 <= self.ball.ycor() <= self.paddle2.ycor()+60:
                self.ball.dx *= -1
                self.ball.dx -= 1
                self.paddle2.s = 'p2a.gif'
                self.paddle2.shape(self.paddle2.s)
                os.system(random.choice(self.sound_list))
                

        # Score player1:
        if self.ball.xcor() > 400:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score1 += 1
            self.pen.clear()
            self.pen.write(f"PlayerA: {self.score1}   PlayerB:{self.score2}", align="center", font=("Courier", 24, "normal"))
            os.system('afplay gong.wav&')
            self.ball.dx = random.choice((-5, 5))

        # Score player2:
        if self.ball.xcor() < -400:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score2 += 1
            self.pen.clear()
            self.pen.write(f"PlayerA: {self.score1}   PlayerB:{self.score2}", align="center", font=("Courier", 24, "normal"))
            os.system('afplay gong.wav&')
            self.ball.dx = random.choice((-5, 5))

        # Game over:
        if self.score1 == 5 or self.score2 == 5:
            self.playing = False
            
            self.pen.clear()
            self.paddle1.goto(1000,1000)
            self.paddle2.goto(1000,1000)
            self.ball.goto(1000,1000)
            self.win.update
            
            self.show_game_over_screen()

    def animate_gif(self):
        
        if self.paddle1.s == 'p1.gif' and self.counter%16 == 0:
            self.paddle1.s = 'p11.gif'
            self.paddle1.shape(self.paddle1.s)
        elif self.paddle1.s == 'p11.gif' and self.counter%18 == 0:
            self.paddle1.s = 'p1.gif'
            self.paddle1.shape(self.paddle1.s)

        if self.paddle2.s == 'p2.gif' and self.counter%13 == 0:
            self.paddle2.s = 'p21.gif'
            self.paddle2.shape(self.paddle2.s)
        elif self.paddle2.s == 'p21.gif' and self.counter%11 == 0:
            self.paddle2.s = 'p2.gif'
            self.paddle2.shape(self.paddle2.s)
        
        self.counter += 1

        # Reset action shape to normal
        if self.ball.xcor()>-200 and self.paddle1.s == 'p1a.gif':
            self.paddle1.s = 'p1.gif'
            self.paddle1.shape(self.paddle1.s)

        if self.ball.xcor()<200 and self.paddle2.s == 'p2a.gif':
            self.paddle2.s = 'p2.gif'
            self.paddle2.shape(self.paddle2.s)

    def show_start_screen(self):
        #self.pen1 = ScoreBoard()
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        self.pic = Paddle(-200, 'p1a.gif')
        self.pic2 = Ball()
        self.pic.goto(0,-100)
        self.pic2.goto(80,-100)
        self.win.update()
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('Karate Pong Game using Python 3 and Turtle\n\n Press the "space" key to continue',
                      align='center', font=('Courier', 24, 'normal'))
            
        self.pic.goto(1000,1000)
        self.pic2.goto(1000,1000)
            
    

    def show_game_over_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        self.pic = Paddle(-200, 'p1a.gif')
        self.pic2 = Ball()
        self.pic.goto(0,-100)
        self.pic2.goto(80,-100)
        self.win.update()
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write(f'       PlayerA: {self.score1} PlayerB:{self.score2} \n\n Press the "space" key for new game',
                      align='center', font=('Courier', 24, 'normal'))
            
        self.pic.goto(1000,1000)
        self.pic2.goto(1000,1000)
            

    def wait_for_keypress(self):
        self.waiting = False

    

game = Game()
game.show_start_screen()


while game.running:
    game.new()
    game.show_game_over_screen()



    
    
