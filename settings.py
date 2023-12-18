class Settings:
    """Class to store all the settings for Alien Invasion """
    def __init__(self):
        """Intialize the game settings"""
        # Screen Settiings
        self.screen_width = 800
        self.screen_height = 800
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
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #How quickly alien value increases 
        self.score_scale = 1.5
        self.intialize_dynamic_settings()
        
    def intialize_dynamic_settings(self):
        """Intialise settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1
            
        #Fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        
        #Score settings
        self.alien_points = 50
            
            
    def increase_speed(self):
        """Increase speed settings & alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_speed = int(self.alien_points * self.score_scale)
        print(self.alien_points)
            
        