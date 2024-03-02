import pygame as pg,sys
from pygame.locals import *
import time

#comments are with "#"

XO = 'x'
Winner = None
Draw = False
width = 400
height = 400
background = (255,255,255)
line_color = (10,10,10)

TBoard = [[None]*3, [None]*3, [None]*3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
Screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe Biatch")

opening = pg.image.load('tictactoe.webp')
x_img = pg.image.load('x.webp')
o_img = pg.image.load('o.webp')

x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    Screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    pg.draw.line(Screen, line_color, (width/3,0), (width/3, height),7)
    pg.draw.line(Screen, line_color, (width/3*2,0), (width/3*2, height),7)

    pg.draw.line(Screen, line_color, (0, height/3), (width, height/3),7)
    pg.draw.line(Screen, line_color, (0, height/3*2), (width, height/3*2),7)
    Draw_status()

def Draw_status():
        global Draw
        
        if Winner is None:
          message = XO.upper() + "'s turn"
        else:
          message = Winner.upper() + " won!"
        if Draw:
            message = 'Draw, you fucked up! :D'

        font = pg.font.Font(None, 30)
        text = font.render(message, 1, (255,255,255))


        Screen.fill ((0,0,0), (0,400,500,100))
        text_rect = text.get_rect(center=(width/2, 500-50))
        Screen.blit(text, text_rect)
        pg.display.update()

def check_win():
    global TBoard, Winner,Draw

    for row in range(0,3):
        if ((TBoard[row][0] == TBoard[row][1] == TBoard[row][2] and(TBoard [row][0] is not None))):
            Winner = TBoard[row][0]
            pg.draw.line(Screen,(250,0,0), (0,(row + 1)*height/3-height/6),(width, (row+1)*height/3-height/6),4)
            break
    for col in range (0, 3):
        if (TBoard[0][col] == TBoard[1][col] == TBoard[2][col]) and (TBoard[0][col] is not None):

            Winner = TBoard[0][col]

            pg.draw.line (Screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                          ((col + 1)* width/3 - width/6, height), 4)
            break

    # check for diagonal winners
    if (TBoard[0][0] == TBoard[1][1] == TBoard[2][2]) and (TBoard[0][0] is not None):
        # game won diagonally left to right
        Winner = TBoard[0][0]
        pg.draw.line (Screen, (250,70,70), (50, 50), (350, 350), 4)

    if (TBoard[0][2] == TBoard[1][1] == TBoard[2][0]) and (TBoard[0][2] is not None):
        # game won diagonally right to left
        Winner = TBoard[0][2]
        pg.draw.line (Screen, (250,70,70), (350, 50), (50, 350), 4)

    if(all([all(row) for row in TBoard]) and Winner is None ):
        draw = True
    Draw_status()

def drawXO(row, col):
    global TBoard, XO
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    TBoard[row-1][col-1] = XO
    if(XO == 'x'):
        Screen.blit(x_img,(posy,posx))
        XO= 'o'
    else:
        Screen.blit(o_img,(posy,posx))
        XO= 'x'
    pg.display.update()
    #print(posx,posy)
    #print(TTT)

def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()

    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None

    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)

    if(row and col and TBoard[row-1][col-1] is None):
        global XO

        drawXO(row,col)
        check_win()
        
def reset_game():
    global TBoard, Winner,XO, Draw
    time.sleep(3)
    XO = 'x'
    Draw= False
    game_opening()
    Winner=None
    TBoard = [[None]*3,[None]*3,[None]*3]
    
game_opening()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            userClick()
            if(Winner or Draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)