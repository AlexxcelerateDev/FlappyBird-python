""""
import pygame

background_image_path = "sprites/background/background.png"

background_image = pygame.image.load(background_image_path)
"""

import pygame

class Background:
    def __init__(self, window_width, window_height, scroll_speed):
        self.image = pygame.image.load("sprites/background/background.png")
        self.image = pygame.transform.scale(self.image, (window_width, window_height))
        self.width = window_width
        self.height = window_height
        self.scroll_speed = scroll_speed
        self.x = 0

    def update(self):
        self.x -= self.scroll_speed
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.width, 0))

