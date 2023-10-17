import pygame
import random

class Pipeline:
    def __init__(self, window_width, window_height, scroll_speed, underground_height,bird_height):
        self.pipelineTop = pygame.image.load("sprites/pipelines/pipeline-top.png") #Tubo arriba
        self.pipelineBottom = pygame.image.load("sprites/pipelines/pipeline-bottom.png") #Tubo abajo
        self.scroll_speed = scroll_speed # velocidad del tubo
        self.x = 0 #Posicion del tubo cada frame

        espacio_cielo_piso = window_height-underground_height
        espacio_entreTubos = espacio_cielo_piso*.3 #Espacio entre ambos tubos

        self.sprite_width_Top, self.sprite_height_Top = self.pipelineBottom.get_size() #Obtiene las dimenciones del tubo arriba
        self.sprite_width_Bottom, self.sprite_height_Bottom = self.pipelineBottom.get_size() #Obtiene las dimenciones del tubo abajo

        #(window_height-underground_height) representa la antura entre el piso y el cielo
        #(window_height-underground_height)*0.1 representa la altura minima que tendrá el tubo de arriba
        #espacio_entreTubos 
        self.min_heightt = (espacio_cielo_piso)-(espacio_cielo_piso)*0.1-espacio_entreTubos 
        
        #Da como resultado una altura aleatoria
        #Inicia la altura minima y la altura maxima
        self.altura_Top = random.randint(int((espacio_cielo_piso)*0.1),int(self.min_heightt))

        self.pipelineTop = pygame.transform.scale(self.pipelineTop, ((window_width)*.1, self.altura_Top))
        
        self.min_height =self.altura_Top+espacio_entreTubos
        self.pipelineBottom = pygame.transform.scale(self.pipelineBottom, (window_width*.1, espacio_cielo_piso-self.min_height+1))
        
        
        #print(self.min_height)
        #print(underground_height)
        #print(self.sprite_height_Bottom)
        self.width = window_width

    def update(self):
        self.x -= self.scroll_speed
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen, width):
        screen.blit(self.pipelineTop, (self.width+self.sprite_width_Top, 0))
        screen.blit(self.pipelineBottom, (self.width+self.sprite_width_Bottom, self.min_height))
        screen.blit(self.pipelineTop, (self.x+self.width, 0))
        screen.blit(self.pipelineBottom, (self.x+self.width, self.min_height))
