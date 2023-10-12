import pygame
import sys
import os
from bird import Bird
from background import Background
from underground import Underground
from pipeline import Pipeline
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
pipeline = Pipeline(WIDTH,HEIGHT,scroll_speed_underground)
bird = Bird(WIDTH, HEIGHT, underground.height)

# Crea una instancia de la clase Bird


# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()  # Llama al método jump cuando se presiona la tecla espacio


    # Lógica del juego


    # Dibujar en la pantalla
    screen.fill(WHITE)
    
    # Lógica de animación
    bird.update()
    background.update()
    underground.update()
    #pipeline.update()
    ####

    # Dibuja el fondo
    background.draw(screen)
    underground.draw(screen, HEIGHT)
    pipeline.draw(screen, WIDTH,HEIGHT-underground.height)
    # Dibuja el sprite actual en la ventana
    # Rota el objeto en función del ángulo
    rotated_bird = pygame.transform.rotate(bird.sprites[bird.current_sprite], bird.angle)
    new_rect = rotated_bird.get_rect(center=(bird.x, bird.y))
    screen.blit(rotated_bird, new_rect.center)
    # Dibuja otros elementos aquí
    
    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()

