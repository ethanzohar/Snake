#Import randint from random
from random import randint

#Function for spawning apples
def appleSpawn(appleX, appleY, BODY_SIZE, countX, countY, segx, segy, sawCount, sawXList, sawYList):
    """ (int, int, int, int, int, list, list, int, list, list) -> (int, int)

    respawns the apples position when given the snakes position, the body size, the saws position, the amount of saws, and the amount of squares on the screen
    """
    appleSet = True #Sets the loop to True
    while appleSet:
        appleIn = False #Says that the apple is not in the snake or the saws
        appleX = randint(1,countX)*BODY_SIZE #Spawns a random x position for the apple
        if appleX/BODY_SIZE % 2 == 0: #Checks to see if it is on the grid
            appleX += BODY_SIZE #Moves the apple onto the grid
        appleY = randint(1,countY)*BODY_SIZE #Spawns a random y position for the apple
        if appleY/BODY_SIZE % 2 == 0: #Checks to see if it is on the grid
            appleY += BODY_SIZE #Moves the aplpe onto the grid
        for i in range(len(segx)): #Checks to see if the apple is in any of the snake's parts
            if appleX == segx[i] and appleY == segy[i]:
                appleIn = True #Says that it is in the snake
        for i in range(sawCount): #checks to see if the apple is in any of the saws
            if appleX == sawXList[i] and appleY == sawYList[i]:
                appleIn = True #Says that it is in the saw
        if appleIn == False: #If the apple is not in the snake or the saws
            return appleX, appleY #Return the apple location
            appleSet = False #Break the loop

#Function for spawning the saws
def sawSpawn(sawXList, sawYList, BODY_SIZE, countX, countY, segx, segy, sawCount, appleX, appleY):
    """ (list, list, int, int, int, list, list, int, int, int) -> (list, list)

    returns the saws position in two lists when given the list of the saws position, the amount of saws, the body size, appleX, appleY, the amount of saws, the amount of squares on the screen, and the snakes position lists
    """
    #Runs for each saw
    for i in range(sawCount):
        sawSet = True #Sets the loop to true
        while sawSet:
            sawIn = False #Says that the saw is not in the snake or the apple
            sawX = randint(1,countX)*BODY_SIZE #Spawns a random x position for the saw
            if sawX/BODY_SIZE % 2 == 0: #Checks to see if it is on the grid
                sawX += BODY_SIZE #Moves the saw onto the grid
            sawY = randint(1,countY)*BODY_SIZE #Spawns a random y position for the saw
            if sawY/BODY_SIZE % 2 == 0: #Checks to see if it is on the grid
                sawY += BODY_SIZE #Moves the saw onto the grid
            for j in range(len(segx)): #Checks to see if it is any of the snake's parts
                if sawX == segx[j] and sawY == segy[j]:
                    sawIn = True #Says that it is in the snake
            if sawX == appleX and sawY == appleY: #Checks to see if it is in the apple
                sawIn = True #Says that it is in the apple
            if sawIn == False: #If the saw is not in the snake or the apple
                sawSet = False #Break the loop

        #Sets the index of the sawList to the new positions
        sawXList[i] = sawX
        sawYList[i] = sawY

    return (sawXList, sawYList) #Returns the new lists

#Function for ending the gamae
def kill(segx, segy, WIDTH, HEIGHT, sawXList, sawYList, startTime, sawCount, realTime):
    """ (list, list, int, int, list, list, int, int, int) -> (bool, bool, bool, bool)

    returns booleans for the game to end when given the snakes position, the saws positions, the dimenstinos of the screen, and the time
    """
    #Deckares the used variables
    game = True
    win = False
    play = True
    gameQuit = False

    #Checks to see if the snake has gone out of the screen
    if segx[0] <= 0 or segx[0] >= WIDTH or segy[0] <= 0 or segy[0] > HEIGHT:
        game = False
        win = True
        play = False
        gameQuit = True

    #Runs through all of the saws
    for i in range(sawCount):
        if segx[0] == sawXList[i] and segy[0] == sawYList[i]: #Checks to see if the snake hit the saw
            game = False
            win = True
            play = False
            gameQuit = True

    #Runs through all of the snakes segments in reverse order
    for i in range(len(segx)-1,0,-1):
        if segx[0] == segx[i] and segy[0] == segy[i]: #Checks to see if the head of the snake hit any of the snake's body parts
            game = False
            win = True
            play = False
            gameQuit = True

    #Checks to see if the time has hit 0
    if startTime - realTime <= 0:
        game = False
        win = True
        play = False
        gameQuit = True

    return (game, win, play, gameQuit) #Returns the variables used to end the game

#Function for getting the snake's images
def snakePicture(snakeBody, segx, segy, speedX, speedY, snakeTail, snake):
    """ (list, list, list, int, int, list, list) -> (list, list)

    returns two lists of pictures when given the snakes x-value, y-value, lists of pictures, and the snakes speed speed
    """
    #Runs for each of the snake's parts except for the head
    for i in range(1,len(snakeBody)+1):
        if i == 1: #If its the body part right after the head
            if segx[i-1] == segx[i] and speedY < 0: #Before piece is above
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[5]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[1]
                else: #After peice is left
                    snakeBody[i-1] = snake[6]
            elif segx[i-1] == segx[i] and speedY > 0: #Before piece is below
                if segx[i+1] == segx[i] and segy[i+1] < segy[i]: #After peice is above
                    snakeBody[i-1] = snake[5]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[2]
                else: #After peice is left
                    snakeBody[i-1] = snake[4]
            elif speedX > 0 and segy[i-1] == segy[i]: #Before piece is right
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[2]
                elif segx[i+1] < segx[i] and segy[i+1] == segy[i]: #After peice is left
                    snakeBody[i-1] = snake[3]
                else: #After peice is above
                    snakeBody[i-1] = snake[1]
            else: #Before piece is left
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[4]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[3]
                else: #After peice is above
                    snakeBody[i-1] = snake[6]
        elif i == len(segx)-1: #If its the tail
            if segx[i-1] == segx[i] and segy[i-1] < segy[i]: #Before piece is above
                snakeTail = snake[11]
            elif segx[i-1] == segx[i] and segy[i-1] > segy[i]: #Before piece is below
                snakeTail = snake[14]
            elif segx[i-1] > segx[i] and segy[i-1] == segy[i]: #Before piece is right
                snakeTail = snake[12]
            else: #Before piece is left
                snakeTail = snake[13]
        else: #If it is a body part that is not right behind the head
            if segx[i-1] == segx[i] and segy[i-1] < segy[i]: #Before piece is above
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[5]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[1]
                else: #After peice is left
                    snakeBody[i-1] = snake[6]
            elif segx[i-1] == segx[i] and segy[i-1] > segy[i]: #Before piece is below
                if segx[i+1] == segx[i] and segy[i+1] < segy[i]: #After peice is above
                    snakeBody[i-1] = snake[5]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[2]
                else: #After peice is left
                    snakeBody[i-1] = snake[4]
            elif segx[i-1] > segx[i] and segy[i-1] == segy[i]: #Before piece is right
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[2]
                elif segx[i+1] < segx[i] and segy[i+1] == segy[i]: #After peice is left
                    snakeBody[i-1] = snake[3]
                else: #After peice is above
                    snakeBody[i-1] = snake[1]
            else: #Before piece is left
                if segx[i+1] == segx[i] and segy[i+1] > segy[i]: #After peice is below
                    snakeBody[i-1] = snake[4]
                elif segx[i+1] > segx[i] and segy[i+1] == segy[i]: #After peice is right
                    snakeBody[i-1] = snake[3]
                else: #After peice is above
                    snakeBody[i-1] = snake[6]
    return snakeBody, snakeTail #Returns the images
