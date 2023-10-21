import pygame

# Establecer una variable de tiempo de enfriamiento en segundos
enfriamiento = 1.0  # 1 segundo de enfriamiento
contador = 0
# Inicializar el temporizador de enfriamiento
tiempo_ultima_colision = 0.0

def detectar_colisiones(objeto1, objeto2):
    global tiempo_ultima_colision

    # Obtener el tiempo actual
    tiempo_actual = pygame.time.get_ticks() / 1000.0  # Convertir el tiempo a segundos

    # Calcular el tiempo transcurrido desde la última colisión
    tiempo_transcurrido = tiempo_actual - tiempo_ultima_colision

    if tiempo_transcurrido >= enfriamiento:
        x1 = objeto1.x
        y1 = objeto1.y
        ancho1 = objeto1.sprite_width
        alto1 = objeto1.sprite_height

        x2 = 0
        y2 = objeto2.y
        ancho2 = objeto2.width
        alto2 = objeto2.height

        if pygame.Rect(x1, y1, ancho1, alto1).colliderect(pygame.Rect(x2, y2, ancho2, alto2)):
            # Manejar la colisión
            print("¡Colisión!")

            # Actualizar el tiempo de la última colisión
            tiempo_ultima_colision = tiempo_actual

def detectar_colisiones_tubos(objeto1, objeto2):
    global tiempo_ultima_colision
    global contador 
    # Obtener el tiempo actual
    tiempo_actual = pygame.time.get_ticks() / 1000.0  # Convertir el tiempo a segundos

    # Calcular el tiempo transcurrido desde la última colisión
    tiempo_transcurrido = tiempo_actual - tiempo_ultima_colision

    if tiempo_transcurrido >= enfriamiento:
        x1 = objeto1.x
        y1 = objeto1.y
        ancho1 = objeto1.sprite_width
        alto1 = objeto1.sprite_height

        pipeline_top = objeto2.pipelineTop.get_rect()

        xTop = objeto2.x+objeto2.width
        yTop = 0
        anchoTop = objeto2.sprite_width_Top
        altoTop = objeto2.sprite_height_Top

        pipeline_bottom = objeto2.pipelineBottom.get_rect()

        xBottom = objeto2.x+objeto2.width
        yBottom = objeto2.min_height
        anchoBottom = objeto2.sprite_width_Bottom
        altoBottom = objeto2.sprite_height_Bottom


        if pygame.Rect(x1, y1, ancho1, alto1).colliderect(pygame.Rect(xTop, yTop, anchoTop, altoTop)):
            # Manejar la colisión
            contador += 1
            print(xTop)
            print(yTop)
            print(anchoTop)
            print(altoTop)

            # Actualizar el tiempo de la última colisión
            tiempo_ultima_colision = tiempo_actual
            return

        if pygame.Rect(x1, y1, ancho1, alto1).colliderect(pygame.Rect(xBottom, yBottom, anchoBottom, altoBottom)):
            # Manejar la colisión
            contador += 1
            print(xBottom)
            print(yBottom)
            print(anchoBottom)
            print(altoBottom)

            # Actualizar el tiempo de la última colisión
            tiempo_ultima_colision = tiempo_actual
            return