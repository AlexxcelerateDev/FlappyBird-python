import pygame
import sys
import random
from bird import Bird
from background import Background
from underground import Underground
from pipeline import Pipeline
from colisiones import detectar_colisiones,detectar_colisiones_tubos
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w*.3, screen_info.current_h*.7
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappybird")
# Configuración de la pantalla
 
# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Colores

# Crea una instancia de la clase Background #0.0015
scroll_speed = WIDTH*0.0015
background = Background(WIDTH, HEIGHT, scroll_speed)

# Crea una instancia de la clase Underground
scroll_speed_underground = scroll_speed *5
underground = Underground(WIDTH, HEIGHT, scroll_speed_underground)
bird = Bird(WIDTH, HEIGHT, underground.height)
pipeline = Pipeline(WIDTH,HEIGHT,scroll_speed_underground,underground.height)

#Arreglo tubos
pipelines = []
#Tiempo de generacion de tubos
tiempo_anterior = pygame.time.get_ticks()  # Tiempo en milisegundos
intervalo_generacion = 2000  # 2000 milisegundos = 2 segundos Genera el tubo inicial

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
    
    # Lógica de animación y movimiento
    bird.update()
    background.update()
    underground.update()
    for objeto in pipelines:
        objeto.update() #Hace que se mueva la tuberia
    ##Colisiones
    detectar_colisiones(bird,underground)
    for objeto in pipelines:
        detectar_colisiones_tubos(bird,objeto)
    ###Colisiones

    # Dibuja el fondo
    background.draw(screen)
    underground.draw(screen)
    # Dibuja el sprite actual en la ventana
    # Rota el pajaro en función del ángulo
    rotated_bird = pygame.transform.rotate(bird.sprites[bird.current_sprite], bird.angle)
    new_rect = rotated_bird.get_rect(center=(bird.x, bird.y))
    screen.blit(rotated_bird, new_rect.center)
    if len(pipelines) >= 1:
        for objeto in pipelines:
            objeto.draw(screen) #Hace que se mueva la tuberia
    #Eleccion entre el de arriba y este:
    """
    for objeto in pipelines:
            objeto.draw(screen) #Hace que se mueva la tuberia
    """
    for objeto in pipelines:
        if(objeto.x <= -objeto.width-objeto.sprite_width_Bottom): #
            pipelines.remove(objeto)
    
    # Lógica para generar tubo cada cierto tiempo
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_anterior >= intervalo_generacion:
        # Generar algo aquí (por ejemplo, un nuevo objeto, evento, o acción)
        pipeline = Pipeline(WIDTH,HEIGHT,scroll_speed_underground,underground.height)
        pipelines.append(pipeline)
        #print(len(pipelines))
        # Actualizar el tiempo anterior para el siguiente ciclo
        tiempo_anterior = tiempo_actual
        intervalo_generacion = random.randint(1000,1500)

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()

