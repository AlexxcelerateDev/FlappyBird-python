import pygame
import random

class Pipeline:
    def __init__(self, window_width, window_height, scroll_speed, underground_height):
        #Atributos
        self.pipelineTop = pygame.image.load("sprites/pipelines/pipeline-top.png") #Tubo arriba
        self.pipelineBottom = pygame.image.load("sprites/pipelines/pipeline-bottom.png") #Tubo abajo
        self.scroll_speed = scroll_speed # velocidad del tubo
        self.x = 0 #Posicion del tubo cada frame

        ###Variables
        espacio_cielo_piso = window_height-underground_height #Trabaja unicamente con el espacio que nos interesa entre el piso y el cielo
        espacio_entreTubos = espacio_cielo_piso*.3 #Espacio entre ambos tubos donde pasará el pajaro

        ###Atributos
        self.sprite_width_Top, self.sprite_height_Top = self.pipelineTop.get_size() #Obtiene las dimenciones del tubo arriba
        self.sprite_width_Bottom, self.sprite_height_Bottom = self.pipelineBottom.get_size() #Obtiene las dimenciones del tubo abajo

        ###Atributos
        #(window_height-underground_height)*0.1 representa la altura minima que tendrá el tubo de abajo (self.pipelineTop)
        #espacio_entreTubos 
        self.min_heightt = (espacio_cielo_piso)-(espacio_cielo_piso)*0.1-espacio_entreTubos 
        
        #Da como resultado una altura aleatoria
        #Inicia la altura minima y la altura maxima espacio_cielo_piso)*0.1 es el tubo de arriba
        self.altura_Top = random.randint(int((espacio_cielo_piso)*0.1),int(self.min_heightt))
        
        #Rescala el tubo Top
        self.pipelineTop = pygame.transform.scale(self.pipelineTop, ((window_width)*.1, self.altura_Top))
        

        self.min_height =self.altura_Top+espacio_entreTubos #Es la altura del tubo bottom
        #Rescala el tubo bottom
        self.pipelineBottom = pygame.transform.scale(self.pipelineBottom, (window_width*.1, espacio_cielo_piso-self.min_height+1))
        
        self.sprite_width_Top, self.sprite_height_Top = self.pipelineTop.get_size() #Obtiene las dimenciones del tubo arriba
        self.sprite_width_Bottom, self.sprite_height_Bottom = self.pipelineBottom.get_size() #Obtiene las dimenciones del tubo abajo
        #print(self.min_height)
        #print(underground_height)
        #print(self.sprite_height_Bottom)
        self.width = window_width
        
    def update(self):
        self.x -= self.scroll_speed #Mueve la tuberia dando efecto de movimiento
    
    #Dibuja al inicio derecho de la pantalla para poder avanzar hasta el final
    def draw(self, screen):
        screen.blit(self.pipelineTop, (self.width+self.sprite_width_Top, 0))
        screen.blit(self.pipelineBottom, (self.width+self.sprite_width_Bottom, self.min_height))
        screen.blit(self.pipelineTop, (self.x+self.width, 0))
        screen.blit(self.pipelineBottom, (self.x+self.width, self.min_height))
