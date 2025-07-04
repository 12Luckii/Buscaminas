import pygame
from biblioteca_funciones import *
from configuraciones import *

pygame.init()
pygame.mixer.init()

pantalla = inicializar_caracteristicas_pantalla(ANCHO_PANTALLA, ALTO_PANTALLA, NOMBRE_JUEGO, RUTA_ICONO_VENTANITA)

pygame.mixer.music.load(RUTA_MUSICA_JUEGO)
pygame.mixer.music.set_volume(0.5)
sonido_victoria = pygame.mixer.Sound(RUTA_MUSICA_VICTORIA)
sonido_derrota = pygame.mixer.Sound(RUTA_MUSICA_DERROTA)
icono_musica_on = pygame.image.load(RUTA_ICONO_MUSICA_ON).convert_alpha()
icono_musica_off = pygame.image.load(RUTA_ICONO_MUSICA_OFF).convert_alpha()


evento_segundo = pygame.USEREVENT + 1
pygame.time.set_timer(evento_segundo, 1000)
fuente_timer = pygame.font.SysFont(FUENTE_DEL_TIMER, TAMANIO_FUENTE_TIMER)



while corriendo_juego:
    eventos = pygame.event.get()
    
    max_ancho_tablero = ANCHO_PANTALLA * 0.9  # que el tablero use hasta 60% ancho pantalla
    max_alto_tablero = ALTO_PANTALLA * 0.9   # y hasta 70% alto pantalla

    for evento in eventos:
        if evento.type == pygame.QUIT:
            corriendo_juego = False

        elif evento.type == evento_segundo:
            if (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and tiempo_inicializado == True and perdi == False and gane == False:
                        segundos += 1
                        if segundos == 60:
                            minutos += 1
                            segundos = 0
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            if pantalla_actual == "Inicio":
                if click_icono_sonido != None and click_icono_sonido.collidepoint(pos) == True:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        musica_activa = False
                    else:
                        pygame.mixer.music.unpause()
                        musica_activa = True
                    continue
                accion = obtener_accion_pantalla_inicio(pantalla, x, y)
                if accion == "Jugar":
                    # pygame.mixer.music.stop()
                    pantalla_actual = "Seleccion niveles"
                elif accion == "Puntajes":
                    # pygame.mixer.music.stop()
                    pantalla_actual = "Puntajes"
                elif accion == "Salir":
                    corriendo_juego = False
                elif accion == "Resolución":
                    cantidad_resoluciones = len(resoluciones)
                    indice_resolucion_actual += 1
                    if indice_resolucion_actual >= cantidad_resoluciones:
                        indice_resolucion_actual = 0
                    nueva_resolucion = resoluciones[indice_resolucion_actual] 
                    ANCHO_PANTALLA = nueva_resolucion[0]
                    ALTO_PANTALLA = nueva_resolucion[1]
                    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

            elif pantalla_actual == "Seleccion niveles":
                accion = obtener_accion_pantalla_niveles(pantalla, x, y)
                if accion == "Facil" or accion == "Medio" or accion == "Dificil":
                    pantalla_actual = accion
                    dificultad_actual = accion
                    matriz_oculta = None
                    minutos = 0
                    segundos = 0
                    mina_explota = None
                    primer_click_realizado = False
                    banderas_colocadas = 0
                    tiempo_inicializado = False
                    perdi = False
                    gane = False
                    
                    if accion == "Facil":
                        filas = 8
                        columnas = 8
                        minas = 10
                        tamanio_celda = 90
                
                    elif accion == "Medio":
                        filas = 16
                        columnas = 16
                        minas = 50
                        tamanio_celda = 45

                    elif accion == "Dificil":
                        filas = 24
                        columnas = 24
                        minas = 120
                        tamanio_celda = 30
                
                    tamanio_celda_ancho = int(max_ancho_tablero / columnas)
                    tamanio_celda_alto = int(max_alto_tablero / filas)
                    
                    if tamanio_celda_ancho < tamanio_celda_alto:
                        tamanio_celda = tamanio_celda_ancho
                    else:
                        tamanio_celda = tamanio_celda_alto
                
                    matriz_oculta = inicializar_matriz(filas, columnas, 0)
                    matriz_visible = inicializar_matriz(filas, columnas, " ")
                    bandera_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_BANDERA, tamanio_celda, tamanio_celda)
                    mina_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_MINA, tamanio_celda,tamanio_celda )
                
                elif accion == "Volver":
                    pantalla_actual = "Inicio"

            elif (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and matriz_oculta != None:
                accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
                
                if accion_buscaminas == "Volver":
                    pantalla_actual = "Inicio"
                elif accion_buscaminas == "Reiniciar":
                    primer_click_realizado = False
                    banderas_colocadas = 0
                    minutos = 0
                    segundos = 0
                    tiempo_inicializado = False
                    mina_explota = None
                    perdi = False
                    gane = False
                    matriz_oculta = inicializar_matriz(filas, columnas, 0)
                    matriz_visible = inicializar_matriz(filas, columnas, " ")
                    pantalla_actual = dificultad_actual
                    
                else:
                    posicion = localizar_posicion_click(evento, filas, columnas, tamanio_celda, 50, 40)
                
                    if posicion != None:
                        pos = posicion
                        fila = pos[0]
                        col = pos[1]

                        if primer_click_realizado == False:
                            if primer_click_realizado == False:
                                matriz_oculta = preparar_tablero_primer_click(matriz_oculta, fila, col, filas, columnas, minas)
                                primer_click_realizado = True
                                tiempo_inicializado = True

                        
                        if evento.button == 1 and matriz_visible[fila][col] != "F":
                                if matriz_oculta [fila][col] == "X":
                                    mina_explota = (fila, col)
                                    revelar_tablero_final(matriz_oculta, matriz_visible)
                                    sonido_derrota.play()
                                    perdi = True
                                    tiempo_transicion = pygame.time.get_ticks()

                                else:
                                    revelar_celdas(matriz_oculta,matriz_visible, fila, col)
                                    if verificar_ganador(matriz_oculta, matriz_visible):
                                        revelar_tablero_final(matriz_oculta,matriz_visible)
                                        sonido_victoria.play()
                                        gane = True
                                        tiempo_transicion = pygame.time.get_ticks()
                        
                        elif evento.button == 3:
                            if matriz_visible[fila][col] == " " and banderas_colocadas < minas:
                                matriz_visible[fila][col]= "F"
                                banderas_colocadas += 1
                            elif matriz_visible[fila][col] == "F":
                                matriz_visible[fila][col] = " "
                                banderas_colocadas -= 1

            elif pantalla_actual == "Puntajes":
                accion = obtener_accion_pantalla_puntajes(pantalla, x, y)
                if accion == "Volver":
                    pantalla_actual = "Inicio"

    # Mostrar pantallas y lógica
    if pantalla_actual == "Inicio":
        ancho = resoluciones[indice_resolucion_actual][0]
        alto = resoluciones[indice_resolucion_actual][1]
        # mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ancho, alto)
        if musica_activa == True and pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play(-1)
        click_icono_sonido = mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ANCHO_PANTALLA, ALTO_PANTALLA, icono_musica_on, icono_musica_off, musica_activa)
        if pantalla_actual != "Inicio":
            pygame.mixer.music.stop()
    
    elif pantalla_actual == "Seleccion niveles":
        mostrar_pantalla_de_niveles(pantalla, RUTA_IMAGEN_SELECCION_DE_NIVELES)

    elif pantalla_actual == "Puntajes":
        fuente_puntitos = pygame.font.SysFont(FUENTE_PUNTITOS_PUNTAJES, TAMANIO_FUENTE_PUNTITOS)
        mostrar_pantalla_de_puntajes(pantalla, RUTA_IMAGEN_PUNTAJES, RUTA_ARCHIVO_PUNTAJES, fuente_puntitos) #fuente creada anteriormente 

    elif pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
        cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)
        x, y = pygame.mouse.get_pos() #chusmea estooO!!!
        accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
        dibujar_buscaminas(pantalla, filas, columnas, COLOR_LINEAS_BUSCAMINAS, COLOR_FONDO_BUSCAMINAS, tamanio_celda, matriz_visible, bandera_buscaminas, mina_buscaminas, mina_explota)
        crear_fondos_de_textos(pantalla, minutos, segundos, COLOR_DEL_TIMER, banderas_colocadas, minas)

    elif pantalla_actual == "Ingresar nombre" and fue_ganador == True:
        total_segundos = minutos * 60 + segundos
        puntaje = calcular_puntaje(dificultad_actual, total_segundos, banderas_colocadas, minas, fue_ganador)
        fuente_puntaje = pygame.font.SysFont(FUENTE_PUNTAJES, TAMANIO_FUENTE_PUNTAJES)
    
        imagen_fondo = pygame.image.load(RUTA_IMAGEN_GANASTE)

        imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())

        nombre_usuario = pedir_nombre_usuario(pantalla, COLO_CAJA_TEXTO_PEDIR_NOMBRE, COLOR_TEXTO_CAJA_PEDIR_NOMBRE, imagen_fondo)
        
        if nombre_usuario != "":
            guardar_puntaje(nombre_usuario, puntaje)
            pantalla_actual = "Puntajes"

    tiempo_actual = pygame.time.get_ticks()
    tiempo = tiempo_actual - tiempo_transicion
    if gane == True and tiempo >= TIEMPO_DE_TRANSICION:
        pantalla_actual ="Ingresar nombre"
        fue_ganador = True
        gane = False

    elif perdi == True and tiempo >= TIEMPO_DE_TRANSICION:
            fue_ganador = False

    actualizar_musica_juego(pantalla_actual, musica_activa)
    pygame.display.update()


pygame.quit()
quit()