import sys

import pygame

from settings import Settings
from ship import Ship

class AllienInvasion:
    """""Overall class to manage game assets and behavior"""

    def __init__(self):
        """""Initialize the gsme, and create game resources"""
        pygame.init()
        self.settings = Settings()
        
        self.ship = Ship(self)
        
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """""Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop        
            self.screen.fill(self.bg_color)
            self.ship.blitme()
                    
if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AllienInvasion
    ai.run_game
