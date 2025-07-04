import pygame
import random as r
from biblioteca_funciones import *

pygame.init()

RESOLUCION_PANTALLA = (1000, 700)
#RESOLUCION_PANTALLA = (1500, 1050) # 50% Incremento
#RESOLUCION_PANTALLA = (500, 350) # 50% Decremento
COLOR_FONDO = (138, 204, 237)
matriz = inicializar_matriz(10, 10, 0)
bandera_matriz = True


pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA)

# Superficie # 94% de la pantalla con bordes de 3%
lado_sup = int(pantalla.get_height() * 0.94)
superficie = pygame.Surface((lado_sup, lado_sup))
superficie.fill("white")


rect_superficie = superficie.get_rect()
margen_superficie = int(pantalla.get_height() * 0.03) # 3% de la pantalla de cada lado
rect_superficie.x = margen_superficie
rect_superficie.y = margen_superficie

if len(matriz) != 0 and len(matriz[0]) != 0:
    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])
    ancho = rect_superficie.w // cant_columnas
    alto = rect_superficie.h // cant_filas

    pos_y = rect_superficie.y + 3
    for i in range(len(matriz)):
        pos_x = rect_superficie.x + 3
        for j in range(len(matriz[i])):
            #color_aleatorio = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            color = (0, 0, 0)
            rectangulo = pygame.Rect(pos_x, pos_y, ancho, alto)
            pos_x += ancho
            matriz[i][j] = {"rect": rectangulo, "color": color}
        pos_y += alto



print(matriz)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j]["rect"].collidepoint(evento.pos) == True:
                        print(f"Coordenada: {i} {j}")
            if rect_superficie.collidepoint(evento.pos) == True:
                print("Estamos sobre la superficie.")


    pantalla.fill(COLOR_FONDO)
    pantalla.blit(superficie, rect_superficie)
    

    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            # pygame.draw.rect(pantalla, matriz[i][j]["color"], matriz[i][j]["rect"]) # SOBRE LA PANTALLA
            pygame.draw.rect(superficie, matriz[k][l]["color"], (matriz[k][l]["rect"].x - margen_superficie, matriz[k][l]["rect"].y - margen_superficie, matriz[k][l]["rect"].w, matriz[k][l]["rect"].h), width=1) # SOBRE LA SUPERFICIE
            # pygame.draw.rect(superficie, matriz[k][l]["color"], matriz[k][l]["rect"], width=2) # SOBRE LA SUPERFICIE

    pygame.display.flip()