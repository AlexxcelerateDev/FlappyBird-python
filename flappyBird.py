import pygame
import sys
import os
from bird import bird
from background import Background
from underground import Underground

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w*.3, screen_info.current_h*.7
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappybird")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Crea una instancia de la clase Background
scroll_speed = 0.5
background = Background(WIDTH, HEIGHT, scroll_speed)

# Crea una instancia de la clase Underground
scroll_speed_underground = scroll_speed *5
underground = Underground(WIDTH, HEIGHT, scroll_speed_underground)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego


    # Dibujar en la pantalla
    screen.fill(WHITE)
    
    # Lógica de animación
    bird.animate_bird()
    background.update()
    underground.update()
    ####
    # Calcula las coordenadas para centrar el sprite
    sprite_width, sprite_height = bird.sprites[bird.current_sprite].get_size()
    x = (WIDTH - sprite_width) // 2  # Centra horizontalmente
    y = (HEIGHT - sprite_height) // 2  # Centra verticalmente

    
    # Dibuja el fondo
    background.draw(screen)
    underground.draw(screen, HEIGHT)

    # Dibuja el sprite actual en la ventana
    screen.blit(bird.sprites[bird.current_sprite], (x, y))

    # Dibuja otros elementos aquí

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()

