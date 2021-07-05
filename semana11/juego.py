#Instalar PyGame: pip install pygame
import sys
import pygame
#Ancho y Alto de la Pantalla
pantalla_x = 800
pabtalla_y = 600
tamanho_pantalla = (pantalla_x,pabtalla_y)
#Inicializar
pygame.init()
#Colores
rgb_blanco = (255,255,255)
rgb_rojo = (255,0,0)
rgb_verde = (0,255,0)
rgb_azul = (0,0,255)
rgb_negro = (0,0,0)
#Centro del Círculo
circulo1_x = 200
circulo1_y = 50
radio_circulo1 = 50
#Punto inicial del Rectángulo
rectangulo_x = 200
rectangulo_y = 200
ancho_rectangulo1 = 150
#Velocidad del círculo
mov_circulo1 = 5
#Velocidad del rectángulo
mov_rectangulo1 = 5
# Reloj: FPS
reloj = pygame.time.Clock()
#Creación de nuestra pantalla
pantalla = pygame.display.set_mode(tamanho_pantalla)
#Juego tiene bucles infinitos o prolongados para mantener activo el juego
while True:
    #Gestión de Eventos: capturar eventos del Mouse y Teclado
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:
            sys.exit()
    #Color de fondo de pantalla
    pantalla.fill(rgb_blanco)
    #Dibujar una recta: [x0,y0],[x1,y1], ancho, alto
    pygame.draw.line(pantalla, rgb_rojo, [0,0], [pantalla_x//4,pabtalla_y//4], 200)
    #Dibujar un rectángulo: x0, y0, ancho, alto
    pygame.draw.rect(pantalla, rgb_verde, (rectangulo_x,rectangulo_y, ancho_rectangulo1, 50))
    #Dibujar un círculo: centro (x0,y0), radio
    pygame.draw.circle(pantalla, rgb_azul, (circulo1_x,circulo1_y), radio_circulo1)
    #Valida que el círculo no se salga de la pantalla: efecto rebote
    if circulo1_x > pantalla_x-radio_circulo1 or circulo1_x-radio_circulo1 < 0:
        mov_circulo1*=-1
    #Valida que el rectángulo no se salga de la pantalla: efecto rebote
    if rectangulo_x+ancho_rectangulo1 > pantalla_x or rectangulo_x<0:
        mov_rectangulo1*=-1

    #Movimiento del círculo
    circulo1_x += mov_circulo1
    # #Movimiento del rectángulo
    rectangulo_x += mov_rectangulo1
    pygame.display.flip()
    #Cantidad de Frames por segundo (FPS)
    reloj.tick(50)