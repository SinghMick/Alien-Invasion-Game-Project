class Game_stats:
    """Track stats for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initiate the stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #High score should be never be reset
        self.high_score = 0
        self.level = 1
        
    def reset_stats(self):
        """Intilize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit 
        self.score = 0
        