import pygame
import os

class Bird:
    def __init__(self, WIDTH, HEIGHT, limit_height):
        # Carga las imágenes (sprites) desde la carpeta
        sprite1 = pygame.image.load(os.path.join(sprites_folder_bird, "bird1.png"))
        sprite2 = pygame.image.load(os.path.join(sprites_folder_bird, "bird2.png"))
        sprite3 = pygame.image.load(os.path.join(sprites_folder_bird, "bird3.png"))

        old_width, old_height = sprite1.get_size() #Tamaño original que se cambiará
        # Factor de escala para el sprite (puedes ajustar este valor)
        factor_de_escala_alto = .05*HEIGHT 
        # Se redimensiona de acuerdo al cambio de la altura
        factor_de_escala_ancho = old_width*(factor_de_escala_alto/old_height)
        # Redimensiona las imágenes en función del factor de escala
        sprite1 = pygame.transform.scale(sprite1, (int(factor_de_escala_ancho), int(factor_de_escala_alto)))
        sprite2 = pygame.transform.scale(sprite2, (int(factor_de_escala_ancho), int(factor_de_escala_alto)))
        sprite3 = pygame.transform.scale(sprite3, (int(factor_de_escala_ancho), int(factor_de_escala_alto)))
        
        self.sprites = [sprite1, sprite2, sprite3]  #Sprites que logran la animacion
        self.current_sprite = 0 # sprite actual de la animacion
        self.animation_speed = 100  # Velocidad inicial (en milisegundos) en este tiempo cambia de sprite a sprite
        self.last_frame_time = pygame.time.get_ticks()  # Tiempo del último cambio de cuadro

        self.sprite_width, self.sprite_height = self.sprites[self.current_sprite].get_size() #obtener la anchura y altura del sprite
        self.x = (WIDTH - self.sprite_width) // 2  # Centra horizontalmente en la pantalla
        self.y = (HEIGHT - self.sprite_height) // 2  # Centra verticalmente en la pantalla
        
        self.HEIGHT= HEIGHT #Obtiene la altura de la pantalla
        ####Cosas añadidas
        self.y_velocity = 0  # Velocidad vertical inicial
        self.gravity = HEIGHT*0.0008  # Valor de la gravedad, puedes ajustarlo según tus necesidades
        self.angle = 0  # Ángulo inicial
        self.current_angle = 0 
        self.bottom_limit = HEIGHT-limit_height-self.sprite_height  # Define el límite inferior de la pantalla, donde choca el sprite abajo
        
        
    ### añadido
    def jump(self):
        # Esta función se llama cuando el pájaro salta  # Cambia la velocidad vertical hacia arriba al saltar
        if self.y > self.sprite_height//4: #solo podrá saltar desde cierta altura
            self.y_velocity = -self.HEIGHT*0.015 #Es el salto

    #Se actualiza en el bucle principal
    def update(self):

        if self.y <= 0:
            self.y = 0

        # Verifica si el pájaro superaría la altura del suelo en el próximo movimiento hacia abajo
        if self.y + self.y_velocity > self.bottom_limit:
            self.y = self.bottom_limit  # Establece la posición del pájaro en la altura del suelo
        else:
            ### añadido
            self.y_velocity += self.gravity  # Aplica la gravedad
            self.y += self.y_velocity  # Actualiza la posición vertical
        ### Carga de sprites (animacion)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.animation_speed:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.last_frame_time = current_time

        # Calcula el ángulo en función de la velocidad vertical
        if self.y_velocity < 0: 
            if self.current_angle < 15:
                self.current_angle += 2
                self.angle = self.current_angle  # Límite máximo hacia abajo
        else:
            if self.current_angle > -15:
                self.current_angle -= 2.5
                self.angle = self.current_angle  # Límite máximo hacia abajo

# Ruta de la carpeta de sprites
sprites_folder_bird = "sprites/bird"