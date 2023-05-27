class Settings():
	#class to store settings for alie invasion game
	def __init__ (self):
		#init game settings
 
		#screen settings
		self.screen_width=1200
		self.screen_height=700
		self.bg_color = (20,20,70)

		#ship settings
		self.ship_speed_factor = 1.5

		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250,60,60
		self.bullets_allowed = 3


		#moje ideje
		self.enemy_height = 20
		self.enemy_width = 20
		self.enemy_color = 30,250,20
