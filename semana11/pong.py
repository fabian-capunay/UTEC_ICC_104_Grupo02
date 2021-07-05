import sys
import pygame
#Inicializar
pygame.init()
#Colores
negro = (0,0,0)
blanco = (255,255,255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
#Ancho y Alto de la Pantalla
pantalla_x = 800
pabtalla_y = 600
tamanho_pantalla = (pantalla_x,pabtalla_y)
#Tamaño estándar de las paletas
ancho_jugador = 15
alto_jugador = 90
#Fuente
fuente = pygame.font.SysFont("Arial", 30)

#Generar la pantalla
pantalla = pygame.display.set_mode(tamanho_pantalla)
#Reloj: FPS
reloj = pygame.time.Clock()
#Coordenadas del jugador 1
jugador1_x = 50
jugador1_y = 300 - (alto_jugador//2)
#Coordenadas del jugador 2
jugador2_x = 750-ancho_jugador
jugador2_y = 300 - (alto_jugador//2)
#Movimiento de los jugadores
mov_jugador1 = 0
mov_jugador2 = 0
#Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
mov_pelota_x = 3
mov_pelota_y = 3
#Flag: bandera de fin del juego
game_over = False

#Puntajes
puntosIzquierdo = 0
puntosDerecho = 0

#Aumentos
AumentoX = 0
AumentoY = 0
aumentoJugadores = 0
while not game_over:
    # Gestión de Eventos: capturar eventos del Mouse y Teclado
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:
            game_over = True
        #Si se presiona una tecla, evaluar
        if evento.type == pygame.KEYDOWN:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = -3 - aumentoJugadores #ir hacia arriba
            if evento.key == pygame.K_s:
                mov_jugador1 = 3 + aumentoJugadores #ir hacia abajo
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = -3 - aumentoJugadores #ir hacia arriba
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 3 + aumentoJugadores #ir hacia abajo
        #Si se deja de presiona la tecla, hay que detener la paleta
        if evento.type == pygame.KEYUP:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = 0 #ir hacia arriba
            if evento.key == pygame.K_s:
                mov_jugador1 = 0 #ir hacia abajo
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = 0 #ir hacia arriba
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 0 #ir hacia abajo

    #Validación de la pelota: efecto rebote
    if pelota_y > 590 or pelota_y < 10:
        mov_pelota_y *=-1
    #Si la pelota sale por el lado izquierdo, o derecho, es porque alguien perdió
    if pelota_x > 800 or pelota_x < 0:
        if pelota_x > 790:
            puntosIzquierdo += 1

        elif pelota_x < 10:
            puntosDerecho += 1
        pelota_x = 400
        pelota_y = 300
        #Si sale de la pantalla, invertimos la dirección
        mov_pelota_x *= -1
        mov_pelota_y *= -1
    #Mover a los jugadores
    jugador1_y += mov_jugador1
    jugador2_y += mov_jugador2
    #Mover la pelota
    pelota_x += mov_pelota_x
    pelota_y += mov_pelota_y
    #Aumentar la velocidad de la pelota
    if mov_pelota_x > 0 and (puntosDerecho + puntosIzquierdo)%2 == 1 and  pelota_x > 790:
        mov_pelota_x += 0.1
        aumentoJugadores += 0.1
    elif mov_pelota_x > 0 and (puntosDerecho + puntosIzquierdo)%2 == 1 and pelota_x < 10:
        mov_pelota_x -= 0.1
        aumentoJugadores += 0.1
    #------------------------------
    # Dibujos
    # ------------------------------
    #Dibujamos el fondo
    pantalla.fill(negro)
    #Dibujamos el jugador 1
    jugador1 = pygame.draw.rect(pantalla, azul, (jugador1_x, jugador1_y, ancho_jugador, alto_jugador))
    #Dibujamos el jugador 2
    jugador2 = pygame.draw.rect(pantalla, azul, (jugador2_x, jugador2_y, ancho_jugador, alto_jugador))
    #Dibujamos la pelota
    pelota = pygame.draw.circle(pantalla, (0, 255, 0), (pelota_x, pelota_y), 10)
    #Puntajes
    texto = fuente.render(f"Jugador 1:   {puntosIzquierdo}        Jugador 2:   {puntosDerecho}", True, rojo)
    pantalla.blit(texto, (215, 50))
    #Detección de colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        mov_pelota_x*= -1
    pygame.display.flip()
    reloj.tick(60)
    if puntosIzquierdo == 10 or puntosDerecho == 10:
        game_over = True
pygame.quit()