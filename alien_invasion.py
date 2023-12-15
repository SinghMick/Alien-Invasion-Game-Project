# Creating a Pygame Window and responding to User inputs 
import sys
import pygame
from settings import Settings 
from ship import Ship 
from bullet import Bullet
from alien import Alien 

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initiate the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        # Set background color 
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            # Watch for keyboard and mouse events
    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet groups"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                     
    def _update_screen(self):
        """Update images on the screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible 
        pygame.display.flip()
    
    def _update_bullets(self):
        """Update position of bullets and get rid of olf bullets"""
        #upadte the bullet position
        self.bullets.update()
          # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)    
        print(len(self.bullets))
    
    def _create_fleet(self):
        """Create a fleet of aliens"""
        print("Creating fleet") 
        #Create an alien and keep adding aliens until there no room left 
        #Spacing between aliens is one alien width and one alien height
        # Make an alien 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width -2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
        #Finished a row ; reset x value, and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
        
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        print("Creating alien")
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
if __name__ == '__main__':
    #Make a game instnace, run the game
    ai = AlienInvasion()
    ai.run_game()