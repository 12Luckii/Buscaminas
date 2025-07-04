import pygame, sys

def creamos_ventana()->None:
    """Documentacion:
    Creamos una ventana de 640x480 con un titulo con el comentario
    'Ventana Basica' """
    
    #INICIALIZO PYGAME
    pygame.init()
    
    pantalla = pygame.display.set_mode((640, 480)) #dimenciones
    pygame.display.set_caption("Ventana Basica 😊👌") #Titulo
    
    imagen_inicio_pantalla = ("BUSCAMINAS_PYGAME/Imagenes/Pantalla inicio.png")
    fondo = pygame.image.load(imagen_inicio_pantalla)
    imagen_escalada = pygame.transform.scale(fondo, (640, 480)) 

    
        # Parámetros del tablero
    FILAS = 8
    COLUMNAS = 8
    TAM_CELDA = 40

    # Estados del juego
    primer_click_realizado = False

    # Lógica del tablero
    # matriz_oculta = inicializar_matriz(FILAS, COLUMNAS, 0)   # Contiene minas y números
    # tablero_visible = inicializar_matriz(FILAS, COLUMNAS, False)  # False = oculto, True = visible
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if evento.type == pygame.KEYDOWN:
                print("Tecla precionada:", pygame.key.name(evento.key)) #Me devuelve el nombre de cada tecla presionada
                # if evento.key == pygame.K_LEFT:
                #     print("Flecha izquierda presionada")
                # if evento.key == pygame.K_UP:
                #     print("Flecha arriba presionada")
                # if evento.key == pygame.K_RIGHT:
                #     print("Flecha derecha presionada")
                # if evento.key == pygame.K_DOWN:
                #     print("Flecha para abajo presionada")
                # if evento.key == pygame.K_SPACE:
                #     print("El espacio presionado")

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # posicion = (evento.pos) #Funciona igual ya que no lo uso para nada, 
                #cuando lo necesite voy a tener que descomentarlo
                # if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    print('Click izquierdo')
                if evento.button == 2:
                    print('Scrol detectado')
                if evento.button == 3:
                    print('Click derecho')
                if evento.button == 4:
                    print('El scrol sube')
                if evento.button == 5:
                    print('El scrol baja')
                
        # pantalla.fill((0, 0, 0))
        pantalla.blit(imagen_escalada, (0, 0))
        
        # for fila in range(FILAS):
        #     for col in range(COLUMNAS):
        #     x = col * TAM_CELDA
        #     y = fila * TAM_CELDA
        #     rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
        
        #     if tablero_visible[fila][col]:
        #         pygame.draw.rect(pantalla, (200, 200, 200), rect)  # Celda descubierta
        #         valor = matriz_oculta[fila][col]
        #     if valor != 0:
        #         fuente = pygame.font.SysFont(None, 24)
        #         texto = fuente.render(str(valor), True, (0, 0, 0))
        #         pantalla.blit(texto, (x + 10, y + 10))
        # else:
        #     pygame.draw.rect(pantalla, (100, 100, 100), rect)  # Celda tapada

        # pygame.draw.rect(pantalla, (0, 0, 0), rect, 1)  # Borde
        
        # sonido_victoria = pygame.mixer.Sound(ruta_sonido)
        # sonido_victoria.set_volume(0.5)
        
        color_verde = (0, 255, 0)
        # coordenadas = (380, 50, 200, 60)
        

        for i in range(4):
            y = 50 + (i * 100)
            coordenadas = (380, y, 200, 60)
            pygame.draw.rect(pantalla, color_verde, coordenadas)

        
        # AMBAS LINEAS HACEN LO MISMO PERO SE ESCRIBEN DIFERENTE, (HABLO DE PYGAME.DRAW.RECT)
        '''¿Cuál conviene usar?
        Depende:
        Si es algo que no cambia y es fijo → podés usarlo en línea (pygame.Rect(...)).
        Si lo vas a usar varias veces, o cambiar su posición 
        o tamaño → conviene guardarlo en una variable como coordenadas.'''

        # pygame.draw.rect(pantalla, color_verde, coordenadas)
        # pygame.draw.rect(pantalla, color_verde, pygame.Rect(60, 150, 100, 60))
        
        # color_verde = (0, 255, 0)
        # coordenadas = (380, 150, 200, 60)
        # pygame.draw.rect(pantalla, color_verde, coordenadas)
        
        # color_verde = (0, 255, 0)
        # coordenadas = (380, 250, 200, 60)
        # pygame.draw.rect(pantalla, color_verde, coordenadas)
        
        # color_verde = (0, 255, 0)
        # coordenadas = (380, 350, 200, 60)
        # pygame.draw.rect(pantalla, color_verde, coordenadas)
        
        '''reduje la repeticion de los rectangulos en un for, ya que lo que estaba haciendo era repetir codigo
        que hacina lo mismo y solo le cambiaba la ubicacion de y, el for esta arriba de los comentarios de .rect()'''
        
        
        # color_azul = (0, 0, 255)
        # coordenadas = (580, 80)
        # radio = 40
        # pygame.draw.circle(pantalla, color_azul, coordenadas, radio)
        
        # color_azul = (0, 0, 255)
        # coordenadas = (580, 180)
        # radio = 40
        # pygame.draw.circle(pantalla, color_azul, coordenadas, radio)
        
        
        pygame.display.update()
        
creamos_ventana()