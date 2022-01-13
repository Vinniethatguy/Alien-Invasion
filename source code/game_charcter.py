import pygame
import os


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        
        path ='/Users/Sutherland/Documents/Python_Work/Projects/Alien_Invasion/images/perry.bmp'
        self.image = pygame.image.load(path)

        #self.image = pygame.image.load('./images/' + 'ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)