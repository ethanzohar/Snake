############################
# Snake Game               #
# By: Ethan Zohar          #
# May 1st 2017             #
# A snake that eats apples #
############################

#---------------#
# Miscellaneous #
#---------------#

#All code for initializing Pygame
import pygame
pygame.init()

#Imports Time
import time

#Imports all the functions for the game
import snakeModule as s

#Imports randint from random
from random import randint

#Sets up the screen window
HEIGHT = 600
WIDTH  = 820
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Sets up the font
font = pygame.font.SysFont("Ariel Black",50)

#Declares all the colours for the game
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED = (255,0,0)
GREY = (128,128,128)
GREEN = (0,255,0)

#Declares all the variables to detect when the game is finished
win = False
play = False
game = True
gameQuit = False

#Sets the delay of the game
delay = 60

#Declares variables that count the amount of squares in the grid on the screen
countX = WIDTH/BODY_SIZE - 1
countY = HEIGHT/BODY_SIZE - 1

#Declares the start time of the game
startTime = 21

#Declares the variable for the players score
score = 0

#Sets the spacebar trigger to True
spaceTrigger = True

#-------#
# Music #
#-------#

#Initializes all of the music for the game
pygame.mixer.music.load('song.wav')  
pygame.mixer.music.set_volume(0.4)  
pygame.mixer.music.play(loops = -1)  
oof = pygame.mixer.Sound('oof2.wav') 
oof.set_volume(10)     
gulp = pygame.mixer.Sound('Gulp.wav') 
gulp.set_volume(10)     

#--------------------#
# Snake's Properties #
#--------------------#

#Declares the body size of the snake
BODY_SIZE = 10

#Declares the variables for the snakes speed/movement
SPEED = 20
speedTrigger = False

#Declares the initial speeds of the snake
speedX = 0
speedY = -SPEED

#Declares the list that holds the snakes x and y positions
segx = [int(WIDTH/2.)]*4
segy = [HEIGHT-BODY_SIZE, HEIGHT+SPEED, HEIGHT+2*SPEED]*4\

#Initializes all the images for the snake
snake = []
for i in range(19):
    snake.append(pygame.image.load('snake' + str(i) + '.png'))
    snake[i] = snake[i].convert_alpha()
    snake[i] = pygame.transform.scale(snake[i], (BODY_SIZE*2, BODY_SIZE*2))

#Sets the different segments of the snake to corrisond to pictures
snakeHead = snake[7]
snakeTail = snake[11]
snakeBody = [snake[5]]*3

#------------------#
# Saw's Properties #
#------------------#

#Declares the initial amount of saws
sawCount = 10

#Declares the lists that hold the x and y positions of the saws
sawXList = []
sawYList = []

#Creates the initial spawn points of the saws
for i in range(sawCount):
    sawX = randint(1,countX)*BODY_SIZE
    if sawX/BODY_SIZE % 2 == 0:
        sawX += BODY_SIZE
    sawXList.append(sawX)
for i in range(sawCount):
    sawY = randint(1,countY)*BODY_SIZE
    if sawY/BODY_SIZE % 2 == 0:
        sawY += BODY_SIZE
    sawYList.append(sawY)

#--------------------#
# Apple's Properties #
#--------------------#

#Declares and creates the initial spawn points of the apple
appleX = randint(1,countX)*BODY_SIZE
if appleX/BODY_SIZE % 2 == 0:
    appleX += BODY_SIZE
appleY = randint(1,countY)*BODY_SIZE
if appleY/BODY_SIZE % 2 == 0:
    appleY += BODY_SIZE

#-----------------------#
# Extra Images and Text #
#-----------------------#

#Declares the image of the saws
saw = pygame.image.load('CoconutMilk.png')
saw = saw.convert_alpha()
saw = pygame.transform.scale(saw, (BODY_SIZE*2, BODY_SIZE*2))

#Declares the image of the apple
apple = pygame.image.load('toms.png')
apple = apple.convert_alpha()
apple = pygame.transform.scale(apple, (BODY_SIZE*2, BODY_SIZE*2))

#Declares the background image
back = pygame.image.load('background1.JPG')
back = back.convert_alpha()
back = pygame.transform.scale(back, (WIDTH, HEIGHT))

#Declares the final screen image
joel = pygame.image.load('joel.png')
joel = joel.convert_alpha()
joel = pygame.transform.scale(joel, (418, HEIGHT))

#Creates the text and position of the intro screen text
introMessage = ['Snake', 'By: Ron Sadovsky', 'Press space to play', 'Rules:', '1. Use the arrow keys to move the snake', '2. Collect the tomers to increase score and time', '3. Don\'t run into the joels, walls, or yourself', '4. Once the timer runs out, you lose!', '5. Survive as long as you can']
introPlace = [(WIDTH/2-60, HEIGHT/2-240),(WIDTH/2-150, HEIGHT/2-200), (WIDTH/2-155, HEIGHT/2-120),(WIDTH/2-60, HEIGHT/2-40),(WIDTH/2-320, HEIGHT/2),(WIDTH/2-390, HEIGHT/2+40),(WIDTH/2-350, HEIGHT/2+80),(WIDTH/2-270, HEIGHT/2+120),(WIDTH/2-220, HEIGHT/2+160)]
introText = []

#-----------------------------------#
# Function That Redraws All Objects #
#-----------------------------------#
def redraw_screen(win, play):
    #Checks to see if game has started playing and if the game has finished
    if play == False and win == False: #If game has yet to begin
        screen.blit(back, (0, 0))
        for i in range(len(introMessage)): #Initialize all intro screen text
            introText.append(font.render(introMessage[i], 1, GREEN))
        for i in range(len(introMessage)): #Draw all intro screen text
            screen.blit(introText[i],introPlace[i])
    elif play == False and win == True: #if game has ended
        screen.blit(back, (0, 0))
        screen.blit(joel,(0,0))
        endMessage = 'I rate that ' + str(score) + ' Rons'
        text3 = font.render(endMessage, 1, GREEN)
        screen.blit(text3, (WIDTH/2-100, HEIGHT-180))
    else: #If game is playing
        screen.blit(back, (0, 0))

        #Draws the snakes head
        screen.blit(snakeHead, (segx[0]-BODY_SIZE, segy[0]-BODY_SIZE))

        #Draws all of the snakes body parts
        for i in range(1,len(segx)-1):
            screen.blit(snakeBody[i-1], (segx[i]-BODY_SIZE, segy[i]-BODY_SIZE))

        #Draws the snakes tail
        screen.blit(snakeTail, (segx[len(segx)-1]-BODY_SIZE, segy[len(segx)-1]-BODY_SIZE))

        #Draws the apple
        screen.blit(apple, (appleX-BODY_SIZE, appleY-BODY_SIZE))

        #Draws all of the saws
        for i in range(sawCount):
            screen.blit(saw, (sawXList[i]-BODY_SIZE, sawYList[i]-BODY_SIZE))

        #Draws the score and the timer on the screen
        message = 'Score: ' + str(score)
        text = font.render(message, 1, WHITE)
        text2 = font.render(timer,1,WHITE)
        screen.blit(text,(10,10))
        screen.blit(text2,(WIDTH-150,0))

    #Updates the display
    pygame.display.update()

#Tells the game to start the main program
inPlay = True

#--------------#
# Main Program #
#--------------#

#The main program loop
while inPlay:
    if game: #If the game has started
        realTime = time.clock() #Start the clock
        timer = 'Time: ' + str(int(startTime - realTime)) #Set the timer text
        
        #Check for events
        for event in pygame.event.get():    #Check for any events
            if event.type == pygame.QUIT:       #If user clicked close
                inPlay = False                #Flag that we are done so we exit this loop

        #Checks to see if the snake ate the apple
        if segx[0] == appleX and segy[0] == appleY:
            gulp.play() #Plays the sound for the apple being eaten
            score+=1 #Add score
            startTime += 5 #Add time to the timer
            (appleX, appleY) = s.appleSpawn(appleX, appleY, BODY_SIZE, countX, countY, segx, segy) #Spawn a new apple
            (sawXList, sawYList) = s.sawSpawn(sawXList, sawYList, BODY_SIZE, countX, countY, segx, segy, sawCount) #Spawn new saws

            #Add three more body parts to the snake
            for i in range(3):
                segx.append(segx[-1])
                segy.append(segy[-1])
            if speedY == 0: #If snake is moving sideways
                for i in range(3):
                    snakeBody.append(snake[3]) #Add 3 sideways images
            else: #If snake is moving vertically
                for i in range(3):
                    snakeBody.append(snake[5]) #Add 3 vertical images
                
        #If the score is an interval of 3
        if score % 3 == 0 and score > 0 and delay > 15:
            #If the score has not already been changed
            if speedTrigger == False:
                delay -= 5 #Increase the speed
                speedTrigger = True #Set the score change to true
        else: #If the score is not an interval of 3
            speedTrigger = False #Set the score change to false

        #Initializes the key presses
        keys = pygame.key.get_pressed()

        #Events for when keys get pressed
        if keys[pygame.K_LEFT] and speedX == 0: #If left is pressed and snake is not moving horizontally
            speedX = -SPEED
            speedY = 0
            snakeHead = snake[8]
        if keys[pygame.K_RIGHT] and speedX == 0: #If right is pressed and snake is not moving horizontally
            speedX = SPEED
            speedY = 0
            snakeHead = snake[9]
        if keys[pygame.K_UP] and speedY == 0: #If up is pressed and snake is not moving vertically
            speedX = 0
            speedY = -SPEED
            snakeHead = snake[7]
        if keys[pygame.K_DOWN] and speedY == 0: #If down is pressed and snake is not moving vertically
            speedX = 0
            speedY = SPEED
            snakeHead = snake[10]
        if keys[pygame.K_SPACE] and spaceTrigger == True: #If space is pressed and it has not already been pressed during the game
            play = True #Start the game
            startTime += realTime #Set the timer back to 20
            spaceTrigger = False #Don't let the spacebar be pressed again

        #Move all segments
        if play == True: #Checks to see if the game is playing
            for i in range(len(segx)-1,0,-1):   #Start from the tail, and go backwards:
                segx[i]=segx[i-1]               #Every segment takes the coordinates
                segy[i]=segy[i-1]               #Of the previous one

            #Changes the pictures of the snake
            (snakeBody, snakeTail) = s.snakePicture(snakeBody, segx, segy, speedX, speedY, snakeTail, snake)

            #Moves the head
            segx[0] = segx[0] + speedX
            segy[0] = segy[0] + speedY

            #Recievies variables from the kill function to see if the game has finished
            (game, win, play, gameQuit) = s.kill(segx, segy, WIDTH, HEIGHT, sawXList, sawYList, startTime, sawCount, realTime)

    #If the game is over
    if gameQuit == True:
        oof.play() #Plays the death sound
        inPlay = False #Ends the main program's loop

    #Update the screen     
    redraw_screen(win, play)
    pygame.time.delay(delay)

pygame.time.delay(2000) #Waits 2 seconds
pygame.mixer.music.stop() #Stops the music
pygame.quit() #Quits the game
