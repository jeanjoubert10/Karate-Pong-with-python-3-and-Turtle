# Pong game with game class allowing start/game over screens
# Jean Joubert 21 Nov 2019
# afplay for mac (winsound for windows)
# written on mac osX - may need speed adjustment on windows
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
import random
import os
#import time # and time.sleep(0.017) windows?

   
class Paddle(turtle.Turtle):
    def __init__(self,xpos, s):
        super().__init__(shape='square')
        self.xpos = xpos
        self.shapesize(5, 1)
        self.color('white')
        self.up()
        self.s = s
        self.goto(self.xpos, 0)
        

    def move_up(self):
        if self.ycor() <= 220:
            self.sety(self.ycor()+50)


    def move_down(self):
        if self.ycor()>= -220:
            self.sety(self.ycor()-50)



class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.up()
        self.color('blue')
        self.dx = random.choice((-5,5)) # May need adjustment in windows eg 0.05
        self.dy = random.choice((-5,5))

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        #if self.xcor() <= -380 or self.xcor() >= 380:
            #self.dx *= -1

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
        # Initialize the game
        self.win = turtle.Screen()
        self.win.setup(800,600)
        self.win.bgcolor('white')
        self.win.title('Karate Pong using python 3 and turtle')
        self.win.tracer(0)
        self.win.listen()
        self.running = True

        self.pen = Scoreboard()

    def new(self):
        # Start new game        
        self.paddle1 = Paddle(-350, 'p1.gif')
        self.paddle2 = Paddle(350, 'p2.gif')
        self.ball = Ball()
        
        self.score1 = 0
        self.score2 = 0

        self.pen.clear()
        self.pen.goto(0,260)
        self.pen.write("PlayerA: 0   PlayerB: 0", align="center", font=("Courier", 24, "normal"))

        self.run()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
           

    def events(self):
        self.win.onkey(self.paddle1.move_up, 'w')
        self.win.onkey(self.paddle1.move_down, 's')
        self.win.onkey(self.paddle2.move_up, 'Up')
        self.win.onkey(self.paddle2.move_down,'Down')
    
    def update(self):
        self.win.update()
        #time.sleep(0.017) # windows?
        
        self.ball.move()

        # Paddle 1 check:
        if (self.paddle1.xcor() <= self.ball.xcor()-10 <= self.paddle1.xcor()+10) and self.ball.dx < 0:
            if self.paddle1.ycor()-60 <= self.ball.ycor() <= self.paddle1.ycor()+60:
                self.ball.dx *= -1
                

        # Paddle 2 check:
        if (self.paddle2.xcor()-10 <= self.ball.xcor() <= self.paddle2.xcor()) and self.ball.dx > 0:
            if self.paddle2.ycor()-60 <= self.ball.ycor() <= self.paddle2.ycor()+60:
                self.ball.dx *= -1


        # Score player1:
        if self.ball.xcor() > 400:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score1 += 1
            self.pen.clear()
            self.pen.write(f"PlayerA: {self.score1}   PlayerB:{self.score2}", align="center", font=("Courier", 24, "normal"))

        # Score player1:
        if self.ball.xcor() < -400:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score2 += 1
            self.pen.clear()
            self.pen.write(f"PlayerA: {self.score1}   PlayerB:{self.score2}", align="center", font=("Courier", 24, "normal"))

        # Game over:
        if self.score1 == 5 or self.score2 == 5:
            self.playing = False
            self.pen.clear()
            self.paddle1.goto(1000,1000)
            self.paddle2.goto(1000,1000)
            self.ball.goto(1000,1000)
            self.win.update
            
            self.show_game_over_screen()

    def show_start_screen(self):
        #self.pen1 = ScoreBoard()
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('Karate Pong Game using Python 3 and Turtle\n\n Press the "space" key to continue',
                      align='center', font=('Courier', 24, 'normal'))
            
    

    def show_game_over_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write(f'       PlayerA: {self.score1} PlayerB:{self.score2} \n\n Press the "space" key for new game',
                      align='center', font=('Courier', 24, 'normal'))
            

    def wait_for_keypress(self):
        self.waiting = False

    

game = Game()
game.show_start_screen()


while game.running:
    game.new()
    game.show_game_over_screen()



    
    
