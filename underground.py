import pygame

class Underground:
    def __init__(self, window_width, window_height, scroll_speed):
        self.image = pygame.image.load("sprites/ground.png") #Carga la imagen
        self.image = pygame.transform.scale(self.image, (window_width, window_height // 6)) #Redimensiona la imagen para que este en el suelo
        self.width = window_width #Ocupara el ancho de la pantalla
        self.height = window_height // 6 #Obtendrá solo ese 
        self.scroll_speed = scroll_speed #La velocidad del suelo
        self.x = 0  #Posicion que logra efecto del movimiento
        self.y = window_height - self.height
    def update(self):
        self.x -= self.scroll_speed #Mueve el suelo
        if self.x <= -self.width:
            self.x = 0 #Vuelve a la posicion inicial
            
    #Dibuja dando el efecto del movimiento
    def draw(self, screen, height):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.width, self.y))