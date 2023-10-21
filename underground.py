import pygame

class Underground:
    def __init__(self, window_width, window_height, scroll_speed):
        self.image1 = pygame.image.load("sprites/ground.png")
        self.image2 = pygame.image.load("sprites/ground.png")
        self.image1 = pygame.transform.scale(self.image1, (window_width, window_height // 6))
        self.image2 = pygame.transform.scale(self.image2, (window_width, window_height // 6))
        self.width = window_width
        self.height = window_height // 6
        self.scroll_speed = scroll_speed
        self.x1 = 0
        self.x2 = self.width - 1  # Ajustar para superponer ligeramente
        self.y = window_height - self.height - 1

    def update(self):
        self.x1 -= self.scroll_speed
        self.x2 -= self.scroll_speed

        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width - 1

        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width - 1

    def draw(self, screen):
        screen.blit(self.image1, (self.x1, self.y))
        screen.blit(self.image2, (self.x2, self.y))
