class Settings:
    """Class to store all the settings for Alien Invasion """
    def __init__(self):
        """Intialize the game settings"""
        # Screen Settiings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #Ship settings
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        