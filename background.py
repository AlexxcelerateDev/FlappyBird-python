""""
import pygame

background_image_path = "sprites/background/background.png"

background_image = pygame.image.load(background_image_path)
"""

import pygame

class Background:
    def __init__(self, window_width, window_height, scroll_speed):
        self.image = pygame.image.load("sprites/background/background.png") #Carga la imagen
        self.image = pygame.transform.scale(self.image, (window_width, window_height)) #Hace la imagen el tamaño de la pantalla
        self.width = window_width   #Tamaño del ancho de la pantalla que tendrá el background
        self.height = window_height #Tamaño de la altura de la pantalla que tendrá el background
        self.scroll_speed = scroll_speed #Velocidad del background
        self.x = 0  # Posicion que logra efecto de velocidad

    def update(self):
        self.x -= self.scroll_speed #se mueve la pantalla dando el efecto
        if self.x <= -self.width:
            self.x = 0 #Vuelve a la posicion inicial

    #Dibuja la imagen dando efecto de movimiento
    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.width, 0))

