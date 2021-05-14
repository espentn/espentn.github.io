#import library
import tkinter as tk
from tkinter import *
import pygame

from pygame.locals import *


window = Tk()
menu = Canvas(window, width = 800, height = 800)
menu.pack() 
img = PhotoImage(file="logo.png")
menu.create_image(20,20,anchor=NW, image=img);

# Player images
pathStr = "c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\"
fileTypeStr = ".png"
playerNames = ["tim", "thea", "andreas", "espen"]
playerImages = [0]*len(playerNames)



startButton = PhotoImage(file = "starte.png")
quitButton = PhotoImage(file = "avslutte.png")

# Define player images
for i in range(len(playerNames)):
	playerImages[i] = [playerNames[i] + fileTypeStr]
	print(playerImages[i])

playerButton = [0]*len(playerImages)
playerButtonImage = [0]*len(playerImages) 
for j in range(len(playerImages)):
	playerButton[j] = PhotoImage(file = playerImages[j])
	playerButtonImage[j] = playerButton[j].subsample(3,3)

# Resize image to fit on button
startButtonImage = startButton.subsample(1, 2)
quitButtonImage = quitButton.subsample(1,2)


def openPlayerWindow1():
	playerWindow = Toplevel(window)
	playerWindow.title("Velg spiller 1")
	playerWindow.geometry("600x800")

	len = 0
	counter = 0
	for k in range(4):
		print(k)
		counter+=1
		Button(playerWindow, image=playerButtonImage[k], command= lambda k=k: getPlayer1(k+1)).place(x=100+len,y=200)
		len+=30

def openPlayerWindow2():
	playerWindow = Toplevel(window)
	playerWindow.title("Velg spiller 2")
	playerWindow.geometry("600x800")

	len = 0
	counter2 = 0
	for x in range(4):
		counter2+=1
		Button(playerWindow, image=playerButtonImage[x], command=lambda x=x: getPlayer2(x+1)).place(x=100+len,y=200)
		len+=30

# Position image on button
Button(menu, image = startButtonImage, command=openPlayerWindow1).place(x=100,y=200)
Button(menu, image = quitButtonImage, ).place(x=110,y=300)

	
def getPlayer1(nameNumber):
	switcher = {
	1: "Tim",
	2: "Thea",
	3: "Andreas",
	4: "Espen"
	}
	playerName1 = switcher.get(nameNumber)
	print(playerName1)
	global player1
	player1 = nameNumber
	openPlayerWindow2()
	return player1

def getPlayer2(nameNumber2):
	switcher = {
	1: "Tim",
	2: "Thea",
	3: "Andreas",
	4: "Espen"
	}
	playerName2 = switcher.get(nameNumber2)
	print(playerName2)
	global player2
	player2 = nameNumber2
	openGameWindow()
	return player2

def openWaitingWindow():
	fpsClock = pygame.time.Clock()

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

def openGameWindow():
	#Initialize game
	pygame.init()

	FPS = 50
	fpsClock = pygame.time.Clock()
	pygame.mixer.music.load('musikk.mp3')
	pygame.mixer.music.play(0)
	global width, height
	width, height = 1700, 1000
	global screen
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

	#load images
	
	bar_image = pygame.image.load("c:\\Users\\io220\\Documents\\Privat\\Python\\Spring break party game\\bar.png")
	print(player1)
	print(player2)
	test = playerImages[player1-1]
	player1Image = pygame.image.load('espen.png')
	player2Image = pygame.image.load('andreas.png')

	font = pygame.font.Font(None, 25)



#Main game loop
	while True:
		screen.fill(1)
		#Calculate elapsed time
		total_seconds = frame_count // frame_rate
		minutes = total_seconds // 60
		seconds = total_seconds % 60
		counting_clock_string = "Tid: {0:02}:{1:02}".format(minutes, seconds)
		text = font.render(counting_clock_string, True, [250, 250, 250])
		screen.blit(text, [600, 10])
		#Show images on screen
		screen.blit(player1Image, player1pos)
		screen.blit(player2Image, player2pos)
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

		player1rect = pygame.Rect(player1Image.get_rect())
		player2rect = pygame.Rect(player2Image.get_rect())
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

window.mainloop()
#while True:
#	screen.fill(0)
#	screen.blit(player, player1pos)