import pygame,sys
#it initilizes pygame.
#i think initialize means to make it able to start
pygame.init()
#i did this so that i dont have to repeat myself when i am coding below
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
blue = [0,0,255]
red = [255 ,0, 0] 
black = [0, 0, 0]
bg_color = [192, 192, 192]
#fonts or texts that are added in
#you know the ones that are dissplayed on screen when someone wins or draws
o_won = pygame.font.SysFont('ariel', 36)
draw = pygame.font.SysFont('ariel', 36)
x_won = pygame.font.SysFont('ariel' , 36)
#this is the screen
screen = pygame.display.set_mode((300 , 250))
#title
pygame.display.set_caption('Tic-Tac-Toe')

#icon
#i dont know what r means but when i had an error i searched on stackoverflow and it said to add r. Then it actually worked so i just stayed with it. I will try to undersatand later but for now just leave it.
cursoro = pygame.image.load(r'C:\Users\Robera\Documents\new\O.png')
#this displays the icon
pygame.display.set_icon(cursoro)
xo = pygame.image.load(r'C:\Users\Robera\Documents\new\X.png')
oo = pygame.image.load(r'C:\Users\Robera\Documents\new\O.png')
#this makes sure that the screen(defined at the top) makes a backgroundcolor.
#i chose light grey because it doesnt make it painful to your eyes when you look at the screen
screen.fill((192, 192, 192))
#invisible boxes are placed so that they can determine the place were it is clicked
#top 3 rectangles
top_left = pygame.draw.rect(screen, bg_color, [0, 0, 100, 83] )
top_center = pygame.draw.rect(screen, bg_color, [100, 0, 100, 83] )
top_right = pygame.draw.rect(screen, bg_color, [200, 0, 100, 83] )
#center 3 rectangles
center_left = pygame.draw.rect(screen, bg_color, [0,83,100,83])
center_center = pygame.draw.rect(screen, bg_color, [100, 83, 100, 83])
center_right = pygame.draw.rect(screen, bg_color , [ 200, 83, 100, 83])
#bottom 3 rectangles
bottom_left = pygame.draw.rect(screen , bg_color, [0, 167,100,83])
bottom_center = pygame.draw.rect(screen, bg_color, [100,167,100,83])
bottom_right = pygame.draw.rect(screen, bg_color, [200, 167, 100,83])
#Game loop so that the window doesnt close down 
running = True
#this is the variable that changes so that there will be handling of turns
turns = 'X'
#global variable so that it easier to determine the win from the draw(to handle instances where there is a win at the last move)
winner = None 
#these are variables that are used to stop overlaying of variables(when i mean variables i mean the values of the rectangle(X) and the value of the circle(O)) on top of eachother
top_left_taken = True
top_center_taken = True
top_right_taken = True
center_left_taken = True
center_center_taken = True 
center_right_taken = True
bottom_left_taken = True
bottom_center_taken = True
bottom_right_taken = True
#
    



#this is the main code

while running:
    #this is saying that for any event in pygame if the "x" button is pressed it should be exited 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
        #this checks for winner
        #make sure to display on the window who won
        #make sure to change to a normal cursor when done
        if board[0] == 1 :
            if board[1] == 1:
                if board[2] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'X'
                    print('X, won')
                
        else:
            pass
        if board[0] == 2:
            if board[1] == 2:
                if board[2] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass            
        #
        if board[3] == 1:
            if board[4] == 1:
                if board[5] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass
        if board[3] == 2:
            if board[4] == 2:
                if board[5] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass            

        if board[6] == 1:
            if board[7] == 1:
                if board[8] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass
        
        if board[6] == 2:
            if board[7] == 2:
                if board[8] ==2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass             
        
        if board[0] == 1:
            if board[3] == 1:
                if board[6] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass
        if board[0] == 2:
            if board[3] == 2:
                if board[6] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass                       
        if board[1] == 1:
            if board[4] == 1:
                if board[7] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass

        if board[1] == 2:
            if board[4] == 2:
                if board[7] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass

        if board[2] == 1:
            if board[5] == 1:
                if board[8] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass

        if board[2] == 2:
            if board[5] == 2:
                if board[8] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass
        #for the diagonals
        if board[0] == 1:
            if board[4] == 1:
                if board[8] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass
        if board[0] == 2:
            if board[4] == 2:
                if board[8] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass
        #
        if board[2] == 1:
            if board[4] == 1:
                if board[6] == 1:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myx = x_won.render('X, won', True, (255, 0, 0), (0, 255, 255))
                    screen.blit(myx,(100, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'x'
                    print('X, won')
        else:
            pass

        if board[2] == 2:
            if board[4] == 2:
                if board[6] == 2:
                    top_left_taken = False
                    top_center_taken = False
                    top_right_taken = False
                    center_left_taken = False
                    center_center_taken = False 
                    center_right_taken = False
                    bottom_left_taken = False
                    bottom_center_taken = False
                    bottom_right_taken = False
                    myo = o_won.render('O,won', True, blue, (255,0,0))
                    screen.blit(myo,(125, 100))
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    winner = 'o'
                    print('O, won')
        else:
            pass    

        if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[7] and board[8] > 0:
            if winner == None:
                print('Draw')
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                mydr = draw.render('Draw',True, (255,255,255), (125, 100))
                screen.blit(mydr,(125, 100))
        
        
        
        
        
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #it prints where it was clicked on the console
            print(pos)
            #this part tells in what section it was clicked in   
            #the top_left_taken and other variables like these athat set as true in the beginning are used here to take only one input(so that is there is no overlaying of the shapes on top of eachother)
            if top_left.collidepoint(pos) and top_left_taken:
                print('Top Left clicked')
                
                if turns == 'X':
                    ##print something on the window to show whose current turn it is       
                    #displays on command of the input of the mouse
                    screen.blit(xo,(25, 5))
                    #this changes so that there is an algorithm to determine the winner by filling in the board
                    board [0] = 1
                    #chnages the turn to another player and also changes cursor
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen , blue, [50, 50], 25)  
                    board [0] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'  
                
                #if this is false then the top will be true and false. 
                #therefore it can no played, and this results in its non-repitition
                top_left_taken = False
                    
            elif top_center.collidepoint(pos) and top_center_taken:
                print('Top Center clicked')
                if turns == 'X':
                    screen.blit(xo,(125, 5))
                    board[1] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue, [150 , 50], 25)
                    board[1] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                top_center_taken = False
            elif top_right.collidepoint(pos) and top_right_taken:
                print('Top right clicked') 
                if turns == 'X':
                    screen.blit(xo,(225, 5))
                    board[2] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)                    
                    turns = 'O'
                else:
                    pygame.draw.circle(screen , blue, [250, 50], 25)
                    board[2] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                top_right_taken = False
            elif center_left.collidepoint(pos):
                print('Center left clicked')
                if turns == 'X' and center_left_taken:
                    screen.blit(xo,(25, 90))
                    board[3] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue, [50, 125], 25)
                    board[3] =2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                center_left_taken = False    
            elif center_center.collidepoint(pos) and center_center_taken:
                print('Center center clicked') 
                if turns == 'X':
                    screen.blit(xo,(125, 90))
                    board[4] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue ,[150 , 125] , 25)
                    board[4] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                center_center_taken = False    
            elif center_right.collidepoint(pos) and center_right_taken:
                print('Center right clicked')
                if turns == 'X':
                    screen.blit(xo,(225, 90))
                    board[5] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue , [250 ,125] ,25)
                    board[5] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                center_right_taken = False    
            elif bottom_left.collidepoint(pos) and bottom_left_taken:
                print('Bottom left clicked')
                if turns == 'X':
                    screen.blit(xo,(25, 175))
                    board[6] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen ,blue ,[50 ,210] ,25)
                    board[6] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                bottom_left_taken = False    
            elif bottom_center.collidepoint(pos) and bottom_center_taken:
                print('Bottom center clicked')
                if turns == 'X':
                    screen.blit(xo,(125, 175))
                    board[7] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue ,[150 , 210], 25)
                    board[7] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                bottom_center_taken = False    
            elif bottom_right.collidepoint(pos) and bottom_right_taken:
                print('Bottom right clicked')                          
                if turns == 'X':
                    screen.blit(xo,(225, 175))
                    board[8] = 1
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    turns = 'O'
                else:
                    pygame.draw.circle(screen, blue, [250, 210], 25)
                    board[8] = 2
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    turns = 'X'
                    bottom_right_taken = False

            #  search a way to import images to represent X and O
            # also find a way to change the cursor on the keyboard when tuns change

                #this shows the chekcing part of the computer to see if there is a winner
                

        

                
    
    




    
    
    #this draws the main frame and will make it easier to divide the window in sections
    pygame.draw.line(screen, black, [100, 0], [100, 250], 5)
    pygame.draw.line(screen, black, [200, 0], [200, 250], 5)
    pygame.draw.line(screen, black, [0, 83], [300, 83], 5)
    pygame.draw.line(screen, black, [0, 167], [300, 167], 5)
    


    #this draws the outline
    pygame.draw.line(screen , black, [0, 0], [0 , 250] , 5)
    pygame.draw.line(screen , black, [0 ,250] , [300, 250] ,5)
    pygame.draw.line(screen , black, [300 ,250] , [300,0] ,5)
    pygame.draw.line(screen,  black, [0, 0], [300, 0], 5)


    








    #it can also be update
    # it runs the program    
    pygame.display.flip()

