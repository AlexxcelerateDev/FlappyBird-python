import pygame
import os

class Bird:
    def __init__(self):
        # Carga las imágenes (sprites) desde la carpeta
        sprite1 = pygame.image.load(os.path.join(sprites_folder_bird, "bird1.png"))
        sprite2 = pygame.image.load(os.path.join(sprites_folder_bird, "bird2.png"))
        sprite3 = pygame.image.load(os.path.join(sprites_folder_bird, "bird3.png"))

        # Factor de escala para el sprite (puedes ajustar este valor)
        factor_de_escala = 3  # Por ejemplo, aumenta el tamaño en un 50%

        # Redimensiona las imágenes en función del factor de escala
        sprite1 = pygame.transform.scale(sprite1, (int(sprite1.get_width() * factor_de_escala), int(sprite1.get_height() * factor_de_escala)))
        sprite2 = pygame.transform.scale(sprite2, (int(sprite2.get_width() * factor_de_escala), int(sprite2.get_height() * factor_de_escala)))
        sprite3 = pygame.transform.scale(sprite3, (int(sprite3.get_width() * factor_de_escala), int(sprite3.get_height() * factor_de_escala)))

        self.sprites = [sprite1, sprite2, sprite3]
        self.current_sprite = 0
        self.animation_speed = 100  # Velocidad inicial (en milisegundos)
        self.last_frame_time = pygame.time.get_ticks()  # Tiempo del último cambio de cuadro
    
    #Realiza la animcacion de los sprites
    def animate_bird(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.animation_speed:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.last_frame_time = current_time

# Ruta de la carpeta de sprites
sprites_folder_bird = "sprites/bird"

# Inicializa Pygame
pygame.init()

# Crea una instancia de la clase Bird
bird = Bird()

"""
import pygame
import os

#bird
sprites_folder_bird = "sprites/bird"
# Carga las imágenes (sprites) desde la carpeta
sprite1 = pygame.image.load(os.path.join(sprites_folder_bird, "bird1.png"))
sprite2 = pygame.image.load(os.path.join(sprites_folder_bird, "bird2.png"))
sprite3 = pygame.image.load(os.path.join(sprites_folder_bird, "bird3.png"))
sprites = [sprite1, sprite2, sprite3]

class Bird:
    def __init__(self):
        self.sprites = sprites
        self.current_sprite = 0
        self.animation_speed = 100  # Velocidad inicial (en milisegundos)
        self.last_frame_time = pygame.time.get_ticks()  # Tiempo del último cambio de cuadro
    
    def animate_bird(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.animation_speed:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.last_frame_time = current_time


bird = Bird()
"""