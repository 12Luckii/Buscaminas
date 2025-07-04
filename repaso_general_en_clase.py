import pygame
import random as r

pygame.init()

ANCHO_PANTALLA = 800 # X
ALTO_PANTALLA = 600  # Y
#               R    G    B
COLOR_FONDO = (102, 233, 237)
COLOR_BOTON = (245, 153, 49)
COLOR_BORDE = (23, 23, 22)
COLOR_TEXTO = (138, 14, 0)
TAMAÑO_Y_PERSONAJE = 0.9


# Superficie es un objeto de pygame
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Mi juego xD")


# Imagenes
ruta_imagen = "Programacion_I_2025/Clase_1/hero.jpg"
imagen_personaje = pygame.image.load(ruta_imagen)
ancho_original = imagen_personaje.get_width()
alto_original = imagen_personaje.get_height()

# Calculo el tamaño del personaje respecto de la pantalla y lo escalo
ALTO_PERSONAJE = int(pantalla.get_height() * TAMAÑO_Y_PERSONAJE)
ANCHO_PERSONAJE = int(ALTO_PERSONAJE * ancho_original / alto_original)
imagen_personaje = pygame.transform.scale(imagen_personaje, (ANCHO_PERSONAJE, ALTO_PERSONAJE))


# Centramos al personaje con atributo del Rect y metodos de Surface:
rect_personaje = imagen_personaje.get_rect()
ubicacion_personaje_x = (pantalla.get_width() / 2) - rect_personaje.center[0]
ubicacion_personaje_y = (pantalla.get_height() / 2) - rect_personaje.center[1]

# Centramos al personaje algoritmicamente:
# ubicacion_personaje_x = (ANCHO_PANTALLA / 2) - (imagen_personaje.get_width() / 2)
# ubicacion_personaje_y = (ALTO_PANTALLA / 2) - (imagen_personaje.get_height() / 2)

# Rectangulo boton
# Rect (x, y, width, height)
rect_boton = pygame.Rect(50, 50, 300, 100)


# Sonidos
# Musica de fondo
ruta_sonido = "Programacion_I_2025/Clase_1/test_sound.mp3"
pygame.mixer.music.load(ruta_sonido)
pygame.mixer.music.set_volume(0.5) # 0 (0%) - 1 (100%)
bandera_musica_fondo = False
# Efectos de Sonido
sonido_victoria = pygame.mixer.Sound(ruta_sonido)
sonido_victoria.set_volume(0.5)

# Texto por pantalla
fuente = pygame.font.SysFont("Arial", 35)
texto_saludo = fuente.render("Hola mundo", True, COLOR_TEXTO)


# Evento Propio / Timer
                #    900 + 1 -> 901
evento_segundo = pygame.USEREVENT + 1
pygame.time.set_timer(evento_segundo, 1000) # 1000 milisegundos = 1 segundo
timer = 0

nombre_usuario = ""
texto_timer = fuente.render(f"Timer: {timer} segundos.", True, COLOR_TEXTO)
bandera_escribir = False
pantalla_principal = True
pantalla_puntajes = False


while True: # Bucle principal del juego.
    if pantalla_principal == True:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == evento_segundo:
                timer += 1
                texto_timer = fuente.render(f"Timer: {timer} segundos.", True, COLOR_TEXTO)

            if evento.type == pygame.MOUSEBUTTONDOWN: # Evento click del mouse

                # Colision con un pixel (coordenada) en la pantalla
                if rect_circulo.collidepoint(evento.pos) == True:
                    print("Clickeaste sobre el circulo, ahora podes ingresar tu nombre.")
                    bandera_escribir = True
                    nombre_usuario = ""

                if boton.collidepoint(evento.pos) == True:
                    pantalla_principal = False
                    pantalla_puntajes = True

                # if evento.button == 1: # Boton izquierdo
                #     print("Descubro una celda en pos:", evento.pos)
                #     # print(pygame.key.get_pressed())
                #     #sonido_victoria.play()
                # elif evento.button == 3: # Boton derecho
                #     print("Pongo/Saco bandera")
            

            
            if evento.type == pygame.KEYDOWN:
                # if evento.key == pygame.K_UP:
                #     print("Guardo puntajes")

                if bandera_escribir == True:
                    if evento.key == pygame.K_RETURN: # Tecla Enter
                        bandera_escribir = False
                        print(nombre_usuario)
                    elif evento.key == pygame.K_BACKSPACE: # Tecla Borrar
                        nombre_usuario = nombre_usuario[0:-1]
                    else:
                        nombre_usuario += evento.unicode


        if bandera_musica_fondo == False:
            # Musica de fondo.
            # pygame.mixer.music.play(-1)
            # pygame.mixer.music.stop()
            # pygame.mixer.music.pause()
            bandera_musica_fondo = True

        # Color de fondo (solido) para la pantalla
        pantalla.fill(COLOR_FONDO)

        # Personaje reajustable
        # ALTO_PERSONAJE = int(pantalla.get_height() * TAMAÑO_Y_PERSONAJE)
        # ANCHO_PERSONAJE = int(ALTO_PERSONAJE * ancho_original / alto_original)
        # imagen_personaje = pygame.transform.scale(imagen_personaje, (ANCHO_PERSONAJE, ALTO_PERSONAJE))

        # Mover elemento por pantalla.
        # ubicacion_personaje_x += 1
        # if ubicacion_personaje_x > ANCHO_PANTALLA:
        #     ubicacion_personaje_x = 0 - imagen_personaje.get_width()
        pantalla.blit(imagen_personaje, (ubicacion_personaje_x, ubicacion_personaje_y))
        
        # Dibujo un rectangulo con su borde.
        boton = pygame.draw.rect(pantalla, COLOR_BOTON, rect_boton, border_radius=15) 
        pygame.draw.rect(pantalla, COLOR_BORDE, rect_boton, width=5, border_radius=15)

        # Genero color aleatorio y dibujo un circulo.
        color_aleatorio = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        rect_circulo = pygame.draw.circle(pantalla, color_aleatorio, (100, 450), 75)

        pantalla.blit(texto_timer, (600, 400))


    if pantalla_puntajes == True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_puntajes = False
                    pantalla_principal = True

        pantalla.fill(COLOR_BOTON)
        texto_volver = fuente.render("Presione ESCAPE para volver.", True, COLOR_BORDE)
        pantalla.blit(texto_volver, (50, 50))

    pygame.display.flip() # Actualiza TODA la pantalla del juego
    # pygame.display.update() # Actualiza TODA la pantalla del juego | Si recibe parametro, actualiza solo ese elemento.
