import pygame

class Underground:
    def __init__(self, window_width, window_height, scroll_speed):
        self.image = pygame.image.load("sprites/ground.png")
        self.image = pygame.transform.scale(self.image, (window_width, window_height // 6))
        self.width = window_width
        self.height = window_height // 6
        self.scroll_speed = scroll_speed
        self.x = 0

    def update(self):
        self.x -= self.scroll_speed
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen, height):
        screen.blit(self.image, (self.x, height - self.height))
        screen.blit(self.image, (self.x + self.width, height - self.height))