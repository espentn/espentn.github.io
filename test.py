#Import library
import pygame
from pygame.locals import *
import random

#Initialize game
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

width, height = 1080, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spring break party game")
keys = [False, False, False, False]
playerpos = [100,100]
acc = [0,0]
arrows = []

badtimer = 100
badtimer1 = 0
badguys = [[width,100]]

frame_count = 0
frame_rate = 60

#Load images
player = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\espen.png")
badguyimg = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\bil.png")
arrow = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\bil.png")

font = pygame.font.Font(None, 25)

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def choose_player():
    screen.fill(0)
    espen = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\espen.png")
    espen2 = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\espen2.png")
   # espen = pygame.transform.scale(espen, (50, 50))

    screen.blit(espen, (50, 50))
    draw_text(screen, "[e]", 25, 130, 165, [250,250,250])
    screen.blit(espen2, (250, 50))
    draw_text(screen, "[t]", 25, 330, 165, [250,250,250])

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                break
            if event.key == pygame.K_t:
                player = espen2
            elif event.key == pygame.K_BACKSPACE:
                screen.fill(0)
                main_menu()
            elif event.key == pygame.K_q:
                pygame.quit()
                
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

def main_menu():
    #background = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\sol.png").convert_alpha()
    #background_rect = background.get_rect()
    title = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\logo.png").convert_alpha()
    title = pygame.transform.scale(title, (width, 81*2))
    avslutte = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\avslutte.png").convert_alpha()
    starte = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\starte.png").convert_alpha()
    #avslutte = pygame.transform.scale(avslutte, (160, 120))
    
#    screen.blit(background, background_rect)
    screen.blit(title, (0,20))
    screen.blit(starte, (55, 320))
    screen.blit(avslutte, (80, 320+50))
    
#    draw_text(screen, "TRYKK [ENTER] FOR Å STARTE", 35, width/2, height/2, [250,250,250])
#    draw_text(screen, "TRYKK [Q] FOR Å AVSLUTTE", 35, width/2, height/2 + 50, [250,250,250])

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                choose_player()
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    
#Keep looping through
            
show_menu = True

while True:
    if show_menu:
        main_menu()
        pygame.time.delay(1000)            
        show_menu = False
        
    badtimer -= 1
    screen.fill(0)

    total_seconds = frame_count //frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    counting_clock_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    text = font.render(counting_clock_string, True, [250,250,250])
    screen.blit(text, [540,10])

    screen.blit(player, playerpos)
    if badtimer==0:
        badguys.append([width, random.randint(50,height)])
        badtimer = 100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0] = True
            elif event.key==K_LEFT:
                keys[1] = True
            elif event.key==K_DOWN:
                keys[2] = True
            elif event.key==K_RIGHT:
                keys[3] = True
            elif event.key==K_SPACE:
                acc[1] += 1
                arrows.append(1)
            elif event.key==K_ESCAPE:
                pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key==K_UP:
                keys[0] = False
            elif event.key==K_LEFT:
                keys[1] = False
            elif event.key==K_DOWN:
                keys[2] = False
            elif event.key==K_RIGHT:
                keys[3] = False
        
    #Move player
    if keys[0]:
        playerpos[1]-=5
    if keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    if keys[3]:
        playerpos[0]+=5
    frame_count += 1
    fpsClock.tick(FPS)
