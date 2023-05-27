import sys
import pygame

 
def check_keydown_events(event,rooster):
	if event.key == pygame.K_RIGHT:
		#move rooster to right
		rooster.moving_right = True
	elif event.key == pygame.K_LEFT:
		rooster.moving_left = True

	#moving up and down
	elif event.key == pygame.K_UP:
		rooster.moving_up = True
	elif event.key == pygame.K_DOWN:
		rooster.moving_down = True





def check_keyup_events(event,rooster):
	if event.key == pygame.K_RIGHT:
		rooster.moving_right = False
	elif event.key == pygame.K_LEFT:
		rooster.moving_left = False

	#not moving up and down
	elif event.key == pygame.K_UP:
		rooster.moving_up = False
	elif event.key == pygame.K_DOWN:
		rooster.moving_down = False


def check_events(rooster):
	#listen for keyboard and mouse events
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,rooster)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,rooster)

def update_screen(ai_settings,screen,rooster):
	#update images on screen and flip to new screen
	screen.fill(ai_settings.bg_color)
	rooster.blitime()

	#make most recent screen visible
	pygame.display.flip()