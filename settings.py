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
        self.ship_limit = 3
        #Bullet Settings
        self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #Alien Settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represents right; -1 represents left;
        self.fleet_direction = 1
        
        