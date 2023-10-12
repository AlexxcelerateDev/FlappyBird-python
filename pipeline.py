import pygame

class Pipeline:
    def __init__(self, window_width, window_height, scroll_speed):
        self.pipelineTop = pygame.image.load("sprites/pipelines/pipeline-top.png")
        self.pipelineBottom = pygame.image.load("sprites/pipelines/pipeline-bottom.png")
        self.scroll_speed = scroll_speed
        self.x = 0
        self.sprite_width, self.sprite_height = self.pipelineBottom.get_size() 

    def update(self):
        self.x -= self.scroll_speed
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen, width ,height):
        screen.blit(self.pipelineTop, (width/2, 0))
        screen.blit(self.pipelineBottom, (width/2, height-self.sprite_height))