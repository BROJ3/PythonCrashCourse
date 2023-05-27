import pygame

import sys
  
from settings import Settings
from rooster import Rooster
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("My_game")

	#make the rooster
	rooster = Rooster(ai_settings, screen)

	while True:
		gf.check_events(rooster)
		rooster.update_position()
		gf.update_screen(ai_settings,screen,rooster)
		
run_game()
