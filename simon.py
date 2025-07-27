'''imports'''
import pygame
import random
import time

'''functions'''
def clear_screen():
    screen.blit(base, BASE_POS)
    instruction()


def comMove(i):
    '''display the color at index i in "colors_list" on the screen'''
    if colors_list[i] == 0:
        screen.blit(red, BASE_POS)
        Rnote.play()
            
    if colors_list[i] == 1: 
        screen.blit(blue, BASE_POS)

        Bnote.play()        
        if colors_list[i] == 2:
                
            screen.blit(green, BASE_POS)
            Gnote.play()

    if colors_list[i] == 3:
            screen.blit(yellow, BASE_POS)
            Ynote.play()

def check():
    ''' checks if player pressed the right button'''
    global colors_list,player_colors_list,i,game_over

    if colors_list[i]!=player_colors_list[i]:
        game_over = True
        

def game_over_screen():
    text_on_screen('GAME OVER',BLACK,[200,250])
    pygame.draw.rect(screen,BLACK,[75,300,450,250])
    text_on_screen('TO PLAY AGAIN -  press "p" ',(255,255,255),[100,375])
    text_on_screen('TO QUIT -  press "q"',(255,255,255),[100,425])

    
def instruction():
    '''display an instruction on screen'''
    global player_turn
    pos = (200,150)
    if player_turn:
        screen.blit(repeat, pos)
    else:
        screen.blit(watch, pos)

    
def newMove():
    ''' adds to the list "colors_list" random color(int)'''
    global colors_list,i
    if i==0:
        colors_list.append(random.randint(0,3))

def player_list():
    '''adds the pressed color to "player_colors_list", and light it on the screen'''
    global player_colors_list
    x,y = pygame.mouse.get_pos()
    color = ((y-300)//230,(x-70)//240)
    
    if color == (0,0):
        player_colors_list.append(0)
        Rnote.play()
        screen.blit(red, BASE_POS)
        
    if color == (0,1):
        player_colors_list.append(1)
        Bnote.play()
        screen.blit(blue, BASE_POS)
        
    if color == (1,0):
        player_colors_list.append(2)
        Gnote.play()
        screen.blit(green, BASE_POS)
        
    if color == (1,1):
        player_colors_list.append(3)
        Ynote.play()
        screen.blit(yellow, BASE_POS)


def restart():
    '''restart all the varibals to play again'''
    global colors_list,player_colors_list,round_num,i,game_over,start_screen,player_turn,play_again
    clear_screen()
    colors_list = []
    player_colors_list = []
    round_num=1
    i=0
    game_over = False
    player_turn=False
    play_again - True
    
def text_on_screen(msg,color,pos):
    ''' display msg on the screen'''
    text = font.render(msg,True,color)
    screen.blit(text,pos)




WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
BASE_POS = (50,300)
BLACK = (0,0,0)
FPS = 30

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simon")
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 30)

'''game board'''
base = pygame.image.load('base.png').convert()
red = pygame.image.load('red.png').convert()
blue = pygame.image.load('blue.png').convert()
green = pygame.image.load('green.png').convert()
yellow = pygame.image.load('yellow.png').convert()
watch = pygame.image.load('watch.png')
repeat = pygame.image.load('repeat.png')

'''sounds'''
pygame.mixer.init()
Rnote = pygame.mixer.Sound('A.wav')
Bnote = pygame.mixer.Sound('E.wav')
Gnote = pygame.mixer.Sound('Elower.wav')
Ynote = pygame.mixer.Sound('C#.wav')


''' start screen'''
start = pygame.image.load('start.png')
screen.blit(start, (0, 0))

colors_list = []
player_colors_list = []
round_num =1
i=0
play_again = False
start_screen = False
player_turn=False
game_over = False
finish=False
delay_time = 0
is_waiting = False

while not finish:
    dt = clock.tick(FPS) / 1000
    x,y = pygame.mouse.get_pos()
    
    if start_screen and not(game_over):
        text_on_screen("round:"+str(round_num),BLACK,[10,10])
        
    for event in pygame.event.get():
        
        if game_over:
            game_over_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    restart()
                elif event.key == pygame.K_q:
                    finish = True

        
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.MOUSEBUTTONDOWN and round_num==1 and not play_again and x>115 and x<460 and y>490 and y<600 :
            start_screen = True
            screen.fill((255,255,255))
            screen.blit(base, BASE_POS)
            
        '''player'''
        if player_turn and i<round_num and not(game_over):
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_list()
                print(i,player_colors_list,'player')
                check()
                if i==round_num-1:
                    i=0
                    player_turn = False
                    player_colors_list.clear()
                    round_num+=1
                    screen.fill((255,255,255))

                else:
                    i+=1
                time.sleep(0.2)


    '''computer'''
    if start_screen and i<round_num and not player_turn and not game_over:
        instruction()
        newMove()
        print(i,colors_list,player_turn,round_num)
        comMove(i)
        is_waiting  = True
        if i==(round_num-1):
            i=0
            player_turn = True
            instruction()
    
        else:
            i+=1
            
        if is_waiting:
            print("waiting")
            delay_time += dt
            if delay_time >= 1:
                print("pass 1")
                clear_screen()
                delay_time = 0
                is_waiting = False
            

    pygame.display.flip()
              

pygame.quit()

    

