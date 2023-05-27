import pygame

class Rooster():
	def __init__ (self, ai_settings, screen):

		#init rooster ad its starting position
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('smallship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start new rooster at the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.center = self.screen_rect.center
		self.rect.height = self.screen_rect.height

		#store a decimal value for ship's center
		self.center = float(self.rect.centerx)
		self.height = float(self.rect.height)

		#movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update_position(self):
		#update position based on movemen flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.rooster_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.rooster_speed_factor


		if self.moving_down and self.rect[1] < 470:
			self.rect[1] += self.ai_settings.rooster_speed_factor

		if self.moving_up and self.rect[1] > 10:
			self.rect[1] -= self.ai_settings.rooster_speed_factor

		#update rect object from self.center
		self.rect.centerx = self.center

	def blitime(self):
		#draw the rooster at its current location
		self.screen.blit(self.image, self.rect)

