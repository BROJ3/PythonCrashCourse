import sys
import pygame

class Settings():
	def __init__ (self):
		self.screen_width=600
		self.screen_height=600
		self.bg_color=(210,210,10)

def check_events():
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Print Statement")

	while True:
		check_events()
		screen.fill(ai_settings.bg_color)
		pygame.display.flip()


run_game()