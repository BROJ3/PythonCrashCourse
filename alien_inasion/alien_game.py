import pygame
import sys
from pygame.sprite import Group

from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf
 
def run_game():
	
	#init game and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien invasion")

	#make a ship
	ship = Ship(ai_settings,screen)

	#make an alien
	alien=Alien(ai_settings,screen)

	#Make a group to store bullets in and a group for aliens
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)

	#start the main loop for running the game
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()
