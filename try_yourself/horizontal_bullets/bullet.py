import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	#class to manage ship bulets
	def __init__ (self, ai_settings, screen, ship):

	#create a bullet at ship's position
		super(Bullet,self).__init__()
		self.screen=screen

		#create a bullet rect at 0,0 and then set correct position
		self.rect = pygame.Rect(0,ship.rect[1]+250,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.left = ship.rect.left + 400

		#store the bullet's position as decimal value
		self.x = float(self.rect.x)
		
		#self.x = float(self.rect.x)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor


	def update(self):
		#move the bullet horizontally across the screen
		self.x+= self.speed_factor

		self.rect.x = self.x


	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)



