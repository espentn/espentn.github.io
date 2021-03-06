#import library
import pygame
from pygame.locals import *

#Initialize game
pygame.init()

FPS = 50
fpsClock = pygame.time.Clock()

width, height = 1700, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spring break party game")
key_player1 = False
key_player2 = False
player1pos = [100,100]
player2pos = [100, 700]
bar1_pos = [1400, 80]
bar2_pos = [1400, 680]
winner = 0

#Time calculation
frame_count = 0
frame_rate = FPS

#Load images
player1 = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\man2.png")
player2 = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\woman.png")
bar_image = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\bar.png")
bar2_image = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\bar.png")

font = pygame.font.Font(None, 25)

#Start menu
def main_menu():
    title = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\logo.png").convert_alpha()
    title = pygame.transform.scale(title, (800, 81*2))
    avslutte = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\avslutte.png").convert_alpha()
    starte = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\starte.png").convert_alpha()
    #avslutte = pygame.transform.scale(avslutte, (160, 120))
    
    screen.blit(title, (width/2-400,20))
    screen.blit(starte, (width/2-528/2, 320))
    screen.blit(avslutte, (width/2-480/2, 320+100))
    
    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

show_menu = True

def get_names():
  player1_name = input("Navn på spiller 1: ")
  player2_name = input("Navn på spiller 2: ")

def show_players():
  screen.fill(0)
  player_espen = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\man_espen2.png") 
  player_andreas = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\man_andreas.png")
  player_tim = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\man_tim.png")
  player_thea = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\woman_thea.png")
  player_espen = pygame.transform.scale(player_espen, (300, 300))
  player_andreas = pygame.transform.scale(player_andreas, (300, 300))
  player_tim = pygame.transform.scale(player_tim, (300, 300))
  player_thea = pygame.transform.scale(player_thea, (300, 300))
  screen.blit(player_espen, (300, 200))
  screen.blit(player_andreas, (600, 200))
  screen.blit(player_tim, (900, 200))
  screen.blit(player_thea, (300, 500))

  pygame.display.update()

  player = player_espen
  while True:
  	event = pygame.event.poll()
  	if event.type == pygame.KEYDOWN:
  		if event.key == pygame.K_e:
  				player = player_espen
  				break
  		elif event.key == pygame.K_a:
  			player = player_andreas
  			break
      #elif event.key == pygame.K_t:
       # player = player_tim
  		elif event.key == pygame.K_q:
  			pygame.quit()
  			sys.exit()
  	elif event.type == QUIT:
  		pygame.quit()
  		sys.exit()
  return player

def winner_screen(pos, minutt, sec):
    player1_win = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\Spiller-1-vant.png").convert_alpha()
    player1_win = pygame.transform.scale(player1_win, (800, 81*2))
    player2_win = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\Spiller-2-vant.png").convert_alpha()
    player2_win = pygame.transform.scale(player2_win, (800, 81*2))
    
    player_win = [player1_win, player2_win]
    screen.blit(player_win[pos], (width/2-400, 320))

    font_winner_clock = pygame.font.SysFont("comicsansms", 72)
    clocker = "Med tiden: {0:02}:{1:02}".format(minutt, sec)
    text = font_winner_clock.render(clocker, True, [250, 250, 250])
    screen.blit(text, [width/2-280, 500])

    pygame.display.update()

show_winnerscreen = True

#Start music
pygame.mixer.music.load('musikk.mp3')
pygame.mixer.music.play(0)

player1_name = input("Navn på spiller 1: ")
player2_name = input("Navn på spiller 2: ")

#Main game loop
while True:
  if show_menu:
    main_menu()
 #   show_players()
    player1 = show_players()
 #   pygame.time.delay(1500)
    show_menu = False

  screen.fill(1)

  #Calculate elapsed time
  total_seconds = frame_count // frame_rate
  minutes = total_seconds // 60
  seconds = total_seconds % 60
  counting_clock_string = "Tid: {0:02}:{1:02}".format(minutes, seconds)
  text = font.render(counting_clock_string, True, [250, 250, 250])
  screen.blit(text, [600, 10])

  #Show images on screen
  screen.blit(player1, player1pos)
  screen.blit(player2, player2pos)
  screen.blit(bar_image, bar1_pos)
  screen.blit(bar_image, bar2_pos)

  pygame.display.flip()
  for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type==pygame.KEYUP:
                if event.key==K_w:
                    key_player1 = True
                    player1pos[0] += 40
                    key_player1 = False
                if event.key==K_RIGHT:
                    key_player2 = True
                    player2pos[0] += 40
                    key_player1 = False

  player1rect = pygame.Rect(player1.get_rect())
  player2rect = pygame.Rect(player2.get_rect())
##  bar_rect = pygame.Rect(bar_image.get_rect())
  player1rect.right = player1pos[0]
  player2rect.right = player2pos[0]
  if player1rect.right > bar1_pos[0]:
    winner = 0
    break

  elif player2rect.right > bar2_pos[0]:
    winner = 1
    break


  frame_count += 1
  fpsClock.tick(FPS)

#Stop music
pygame.mixer.music.stop()

# effect = pygame.mixer.Sound('tim.m4a')
# effect.play()
#Show winner of game
screen.fill(0)
winner_screen(winner, minutes, seconds)

f = open("Resultater.txt", 'a')
if winner == 0:
  f.write("{} {}:{} \n".format(player1_name, minutes, seconds))
  f.close()

pygame.time.delay(3000)