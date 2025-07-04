import pygame
import random

#CARACTERISTICAS PANTALLA
def inicializar_caracteristicas_pantalla(ancho:int, largo:int, titulo_juego:str, ruta_icono:str) -> pygame.Surface: 
    """
    Esta función permite inicializar la pantalla en general.
    
    Recibe:
        ancho (int): ancho de la pantalla.       
        largo (int): largo de la pantalla.
        titulo_juego (str): titulo del juego, en este caso, "Buscaminas".
        ruta_icono (str):imagen del icono de la ventanita.
    
    Retorna:
        pygame.Surface: superficie de la pantalla.
    
    """
    pantalla = pygame.display.set_mode((ancho, largo))
    pygame.display.set_caption(titulo_juego)
    icono_ventana = pygame.image.load(ruta_icono)
    pygame.display.set_icon(icono_ventana)

    return pantalla

#PANTALLA INICIO REHACERRRR
def dibujar_boton(pantalla:pygame.Surface, x:int, y:int, ancho:int, alto:int, texto:str, color_boton:tuple, color_texto:tuple, borde_redondeado:int=40) -> None:
    """
    Esta función permite dibujar un boton.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en al cual se quiere dibujar el boton.
        x (int): coordenada horizontal en donde se va a ubicar el boton.
        y (int): coordenada vertical en donde se va a ubicar el boton.
        ancho (int): ancho del boton.
        alto (int): alto del boton.
        texto (str): texto que va estar adentro de ese boton.
        color_boton (tuple): color del botón.
        color_texto (tuple): color del texto.
        borde_redondeado:(int=40): redondez del boton 
    """

    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto), border_radius=borde_redondeado) #fijate #, width=5, border_radius=10
    pygame.draw.rect(pantalla, (0,0,0), (x,y, ancho, alto), width=3, border_radius=borde_redondeado)

    tamanio_fuente = int(alto * 0.4)
    fuente_letras = pygame.font.SysFont("Arial", tamanio_fuente)
    texto = fuente_letras.render(texto, True, color_texto)

    texto_rectangulo = texto.get_rect(center=(x + ancho // 2, y + alto // 2))

    pantalla.blit(texto, texto_rectangulo)


def calcular_posiciones_botones_inicio(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los botones de la pantalla de inicio para poder redimensionarlos .
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual están los botones.
    
    Retorna:
        dict: diccionario con claves y valores de los botones.
    
    """
    
    tamanio_pantalla = pantalla.get_size()
    ancho_pantalla = tamanio_pantalla[0]
    alto_pantalla = tamanio_pantalla[1]

    diccionario =  {"ancho_boton": int(ancho_pantalla * 0.326),
                    "alto_boton": int(alto_pantalla * 0.150),
                    "espacio_entre_botones": int(alto_pantalla * 0.062),
                    "posicion_horizontal_boton": int(ancho_pantalla * 0.598),
                    "posicion_vertical_boton": int(alto_pantalla * 0.180),
                    "ancho_boton_resolucion": int(ancho_pantalla * 0.25),
                    "alto_boton_resolucion": int(alto_pantalla * 0.10),
                    "posicion_horizontal_resolucion": int(ancho_pantalla * 0.64),
                    "posicion_vertical_resolucion": int(alto_pantalla * 0.05)}

    return diccionario

#Agregué esto!!!!!!!!!!!
def calcular_posicion_icono_audio(pantalla:pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones del icono del audio de la pantalla de inicio para poder redimensionarlos .
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual está el icono.
    
    Retorna:
        dict: diccionario con claves y valores del icono.
    
    """
    tamanio_pantalla = pantalla.get_size()
    ancho_pantalla = tamanio_pantalla[0]
    alto_pantalla = tamanio_pantalla[1]

    diccionario = {"lado_icono_sonido": int(alto_pantalla * 0.090),
                    "posicion_x_icono_sonido": int(ancho_pantalla *0.93),
                    "posicion_y_icono_sonido": int(alto_pantalla * 0.025)}#2.5

    return diccionario

def actualizar_musica_juego(pantalla_actual:str, musica_activa:bool) -> None:
    """
    Esta función permite actualizar la musica del juego.
    
    Recibe:
        pantalla_actual (str): pantalla en la cual está la musica.
        musica_activa (bool): si la música está activa o no.

    """
    if musica_activa == True and (pantalla_actual == "Inicio" or pantalla_actual == "Seleccion niveles" or pantalla_actual == "Puntajes"):
        if pygame.mixer.music.get_busy() == False: #Si no se está reproduciendo música
            pygame.mixer.music.play(-1) #Entonces la inicia en bucle infinito
    else:
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()

def mostrar_pantalla_inicio(pantalla:pygame.Surface, ruta_imagen:str, ancho:int, alto:int, icono_musica_on:str, icono_musica_off:str, audio_on: bool) -> pygame.Rect:
    """
    Esta función permite mostrar la pantalla de inicio, incluido con los botones.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se van a mostrar los elementos.
        ruta_imagen (str): imagen de fondo.
        ancho (int): ancho de la pantalla.
        alto (int): alto de la pantalla.
        icono_musica_on (str): ruta imagen icono musica on.
        icono_musica_off (str): ruta imagen icono musica off.
        audio_on (bool): si el audio está sonando.
    
    Retorna:
        pygame.Rect: para obtener el collidepoint del icono de musica.
    
    """
    imagen_inicio = pygame.image.load(ruta_imagen)
    imagen_inicio  = pygame.transform.scale(imagen_inicio, pantalla.get_size())
    pantalla.blit(imagen_inicio, (0,0))

    texto_resolucion = f"Resolución: {ancho} X {alto}"

    posiciones = calcular_posiciones_botones_inicio(pantalla)

    ancho_boton = posiciones["ancho_boton"]
    alto_boton = posiciones["alto_boton"]
    espacio_entre_botones = posiciones["espacio_entre_botones"]
    posicion_horizontal_boton = posiciones["posicion_horizontal_boton"]
    posicion_vertical_boton = posiciones["posicion_vertical_boton"]
    ancho_boton_resolucion = posiciones["ancho_boton_resolucion"]
    alto_boton_resolucion = posiciones["alto_boton_resolucion"]
    posicion_horizontal_resolucion = posiciones["posicion_horizontal_resolucion"]
    posicion_vertical_resolucion = posiciones["posicion_vertical_resolucion"]

    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton, ancho_boton, alto_boton, "Jugar", (169, 156, 140), (156, 106, 69))
    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton + 1*(alto_boton + espacio_entre_botones), ancho_boton, alto_boton, "Puntajes", (169, 156, 140), (156, 106, 69))
    dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton + 2*(alto_boton + espacio_entre_botones), ancho_boton, alto_boton, "Salir", (169, 156, 140), (156, 106, 69))
    dibujar_boton(pantalla, posicion_horizontal_resolucion, posicion_vertical_resolucion + 5*(alto_boton_resolucion + espacio_entre_botones), ancho_boton_resolucion, alto_boton_resolucion, texto_resolucion, (169, 156, 140), (156, 106, 69))

    posicion_icono = calcular_posicion_icono_audio(pantalla)
    if audio_on == True:
        icono_actual = icono_musica_on
    else:
        icono_actual = icono_musica_off
    lado = posicion_icono["lado_icono_sonido"]
    icono_escalado = pygame.transform.smoothscale(icono_actual, (lado,lado))
    pantalla.blit(icono_escalado, (posicion_icono["posicion_x_icono_sonido"], posicion_icono["posicion_y_icono_sonido"]))
    
    return pygame.Rect(posicion_icono["posicion_x_icono_sonido"], posicion_icono["posicion_y_icono_sonido"], lado, lado)

def obtener_accion_pantalla_inicio(pantalla: pygame.Surface, x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla de inicio.

    Recibe:
        x (int): coordenada horizontal en donde se hizo click.
        y (int): coordenada vertical en donde se hizo click.

    Retorna:
        str: acción a realizar según click del mouse.
    """
    accion = None

    posiciones = calcular_posiciones_botones_inicio(pantalla)
    
    ancho_del_boton = posiciones["ancho_boton"]
    alto_del_boton = posiciones["alto_boton"]
    espacios_entre_los_botones = posiciones["espacio_entre_botones"]
    posicion_horizontal_boton = posiciones["posicion_horizontal_boton"]
    posicion_vertical_inicial_boton = posiciones["posicion_vertical_boton"]
    ancho_res = posiciones["ancho_boton_resolucion"]
    alto_res = posiciones["alto_boton_resolucion"]
    posicion_horizontal_resolucion = posiciones["posicion_horizontal_resolucion"]
    posicion_vertical_resolucion = posiciones["posicion_vertical_resolucion"]

    if (x >= posicion_horizontal_boton) and (x <= posicion_horizontal_boton + ancho_del_boton):
        if ((y >= posicion_vertical_inicial_boton) and (y <= posicion_vertical_inicial_boton + alto_del_boton)):
            accion = "Jugar"
        elif ((y >= posicion_vertical_inicial_boton + alto_del_boton + espacios_entre_los_botones) and (y <= posicion_vertical_inicial_boton + 2*(alto_del_boton + espacios_entre_los_botones))):
            accion = "Puntajes"
        elif ((y >= posicion_vertical_inicial_boton + 2 *(alto_del_boton + espacios_entre_los_botones)) and (y <= posicion_vertical_inicial_boton + 3*(alto_del_boton + espacios_entre_los_botones))):
            accion = "Salir"
        elif ((x >= posicion_horizontal_resolucion) and (x <= posicion_horizontal_resolucion + ancho_res) and (y >= posicion_vertical_resolucion + 5 * (alto_res + espacios_entre_los_botones)) and (y <= posicion_vertical_resolucion + 5 * (alto_res + espacios_entre_los_botones) + alto_res)):
            accion = "Resolución"
    
    return accion


#PANTALLAS SELECCION DE NIVELES
def calcular_posiciones_botones_niveles(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los botones de la pantalla de selección de niveles para poder redimensionarlos .
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual están los botones.
    
    Retorna:
        dict: diccionario con claves y valores de los botones.
    
    """
    tamanio_pantalla = pantalla.get_size()
    ancho_pantalla = tamanio_pantalla[0]
    alto_pantalla = tamanio_pantalla[1]
    
    diccionario = {"ancho_boton_nivel": int(ancho_pantalla * 0.261),    # Ejemplo: 25% ancho pantalla
                    "alto_boton_nivel": int(alto_pantalla * 0.187),      # Ejemplo: 18% alto pantalla
                    "ancho_boton_volver": int(ancho_pantalla * 0.130),
                    "alto_boton_volver": int(alto_pantalla * 0.125),
                    "posicion_x_facil": int(ancho_pantalla * 0.261),
                    "posicion_y_facil": int(alto_pantalla * 0.312),
                    "posicion_x_medio": int(ancho_pantalla * 0.619),
                    "posicion_y_medio": int(alto_pantalla * 0.312),
                    "posicion_x_dificil": int(ancho_pantalla * 0.424),
                    "posicion_y_dificil": int(alto_pantalla * 0.562),
                    "posicion_x_volver": int(ancho_pantalla * 0.782),
                    "posicion_y_volver": int(alto_pantalla * 0.843)}
    
    return diccionario


def mostrar_pantalla_de_niveles(pantalla:pygame.Surface, ruta_imagen:str) -> None:
    """
    Esta función permite mostrar la pantalla de seleccion de los niveles, incluidos sus botones.
    
    Recibe:
        pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
        ruta_imagen (str): imagen de fondo de la pantalla de seleccion de niveles.

    """
    imagen_seleccion_de_niveles = pygame.image.load(ruta_imagen)
    imagen_seleccion_de_niveles = pygame.transform.scale(imagen_seleccion_de_niveles, pantalla.get_size())
    pantalla.blit(imagen_seleccion_de_niveles, (0,0))

    posiciones = calcular_posiciones_botones_niveles(pantalla)

    dibujar_boton(pantalla, posiciones["posicion_x_facil"], posiciones["posicion_y_facil"], posiciones["ancho_boton_nivel"], posiciones["alto_boton_nivel"], "Facil", (55,41,22), (156,106,69))
    dibujar_boton(pantalla, posiciones["posicion_x_medio"], posiciones["posicion_y_medio"], posiciones["ancho_boton_nivel"], posiciones["alto_boton_nivel"], "Medio", (55,41,22), (156,106,69))
    dibujar_boton(pantalla, posiciones["posicion_x_dificil"], posiciones["posicion_y_dificil"], posiciones["ancho_boton_nivel"], posiciones["alto_boton_nivel"], "Dificil", (55,41,22), (156,106,69))
    dibujar_boton(pantalla, posiciones["posicion_x_volver"], posiciones["posicion_y_volver"], posiciones["ancho_boton_volver"], posiciones["alto_boton_volver"], "Volver", (55,41,22), (156,106,69))


def obtener_accion_pantalla_niveles(pantalla:pygame.Surface, x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla de seleccion de niveles.
    
    Recibe:
        La pantalla: pygame.Surface
        x (int): coordenada horizontal en donde se hizo click.
        y (int): coordenada vertical en donde se hizo click.
    
    Retorna:
        str: acción a realizar según click del mouse.
    
    """
    accion = None
    
    posiciones = calcular_posiciones_botones_niveles(pantalla)
    
    ancho_botones_niveles = posiciones["ancho_boton_nivel"]
    alto_botones_niveles = posiciones["alto_boton_nivel"]
    ancho_boton_volver = posiciones["ancho_boton_volver"]
    alto_boton_volver = posiciones["alto_boton_volver"]
    
    posicion_x_facil = posiciones["posicion_x_facil"]
    posicion_y_facil = posiciones["posicion_y_facil"]
    posicion_x_medio = posiciones["posicion_x_medio"]
    posicion_y_medio = posiciones["posicion_y_medio"]
    posicion_x_dificil = posiciones["posicion_x_dificil"]
    posicion_y_dificil = posiciones["posicion_y_dificil"]
    posicion_x_volver = posiciones["posicion_x_volver"]
    posicion_y_volver = posiciones["posicion_y_volver"]

    if ((x >= posicion_x_facil) and (x <= posicion_x_facil + ancho_botones_niveles) and (y >= posicion_y_facil) and (y <= posicion_y_facil + alto_botones_niveles)):
        accion = "Facil"
    elif ((x >= posicion_x_medio) and (x <= posicion_x_medio + ancho_botones_niveles) and (y >= posicion_y_medio) and (y <= posicion_y_medio + alto_botones_niveles)):
        accion = "Medio"
    elif ((x >= posicion_x_dificil) and (x <= posicion_x_dificil + ancho_botones_niveles) and (y >= posicion_y_dificil) and (y <= posicion_y_dificil + alto_botones_niveles)):
        accion = "Dificil"
    elif ((x >= posicion_x_volver) and (x <= posicion_x_volver + ancho_boton_volver) and (y >= posicion_y_volver) and (y <= posicion_y_volver + alto_boton_volver)):
        accion = "Volver"
    return accion

def calcular_posiciones_botones_inicio_fondo(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los botones de la pantalla de  para poder redimensionarlos.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual están los botones.
    
    Retorna:
        dict: diccionario con claves y valores de los botones.
    
    """
    
    tamanio = pantalla.get_size()
    ancho_pantalla = tamanio[0]
    alto_pantalla = tamanio[1]
    
    posiciones = {"ancho_boton_volver": int(ancho_pantalla * 0.3),
            "alto_boton_volver": int(alto_pantalla * 0.12),
            "posicion_x_volver": int(ancho_pantalla * 0.61),
            "posicion_y_volver": int(alto_pantalla * 0.8),
            "ancho_boton_reiniciar": int(ancho_pantalla * 0.3),
            "alto_boton_reiniciar": int(alto_pantalla * 0.12),
            "posicion_x_reiniciar": int(ancho_pantalla * 0.61),
            "posicion_y_reiniciar": int(alto_pantalla * 0.65)}

    return posiciones


#PANTALLA NIVEL ELEGIDO
def cargar_fondo_segun_nivel_elegido(pantalla:pygame.Surface, nivel:str, color_texto:tuple=(255, 255, 255), color_fondo_boton:tuple=(0, 0, 0)) -> pygame.Surface: #?
    """
    Esta función permite cargar el fondo de pantalla segun el nivel que se elige.
    
    Recibe:
        pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
        nivel (str): nivel elegido.
        color_texto (tuple): color del texto.
        color_fondo_boton (tuple): color del fondo del botón.
        
    Retorna:
        pygame.Surface: superficie de la pantalla.
    
    """

    if nivel == "Facil":
        imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nivel_facil.png")

    elif nivel == "Medio":
        imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nievel_medio.png")

    elif nivel == "Dificil":
        imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nivel_dificil.png") 

    imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())
    pantalla.blit(imagen_fondo, (0,0))

    posiciones = calcular_posiciones_botones_inicio_fondo(pantalla)
    
    dibujar_boton(pantalla, posiciones["posicion_x_volver"], posiciones["posicion_y_volver"], posiciones["ancho_boton_volver"], posiciones["alto_boton_volver"], "Volver", color_fondo_boton, color_texto)
    dibujar_boton(pantalla, posiciones["posicion_x_reiniciar"], posiciones["posicion_y_reiniciar"], posiciones["ancho_boton_reiniciar"], posiciones["alto_boton_reiniciar"], "Reiniciar", color_fondo_boton, color_texto)

    return imagen_fondo


#BUSCAMINAS
def calcular_posiciones_fondos_textos(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los fondos (rectangulares) y textos de la pantalla de juego para poder redimensionarlos .
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual están los fondos.
    
    Retorna:
        dict: diccionario con claves y valores de los botones.
    
    """
    
    tamanio_pantalla = pantalla.get_size()
    ancho_pantalla = tamanio_pantalla[0]
    alto_pantalla = tamanio_pantalla[1]
    
    diccionario = {"x_timer": int(ancho_pantalla * 0.600),
                    "y_timer": int(alto_pantalla * 0.100),
                    "ancho_timer": int(ancho_pantalla * 0.326),
                    "alto_timer": int(alto_pantalla * 0.125),
                    "x_banderas": int(ancho_pantalla * 0.600),
                    "y_banderas": int(alto_pantalla * 0.312),
                    "ancho_banderas": int(ancho_pantalla * 0.326),
                    "alto_banderas": int(alto_pantalla * 0.125)}

    return diccionario


def crear_fondos_de_textos(pantalla:pygame.Surface, minutos:int, segundos:int, color_timer:tuple, banderas_colocadas:int, minas:int) -> None:
    """
    Esta función permite crear los fondos para los textos de la pantalla de juego.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se dibujan los fondos.
        timer (int): timer que se pone arriba del fondo.
        fuente_timer (pygame.font.Font): fuente del timer.
        color_timer (tuple): color del texto del timer.
        banderas_colocadas (int): texto de banderas.
        minas (int): minas colocadas.

    """
    posiciones = calcular_posiciones_fondos_textos(pantalla)

    rectangulo_timer = pygame.Rect(posiciones["x_timer"], posiciones["y_timer"], posiciones["ancho_timer"], posiciones["alto_timer"])
    pygame.draw.rect(pantalla, (0,0,0), rectangulo_timer)

    rectangulo_banderas = pygame.Rect(posiciones["x_banderas"], posiciones["y_banderas"], posiciones["ancho_banderas"], posiciones["alto_banderas"])
    pygame.draw.rect(pantalla, (0,0,0), rectangulo_banderas)

    tamanio = pantalla.get_size()
    alto_pantalla = tamanio[1]

    tamanio_fuente_timer = int(alto_pantalla * 0.06)  # 6% de la altura
    fuente_timer = pygame.font.SysFont("Arial", tamanio_fuente_timer)
    texto_timer = crear_texto_timer(minutos, segundos, fuente_timer, color_timer)
    rectangulo_texto_timer = texto_timer.get_rect()
    rectangulo_texto_timer.center = rectangulo_timer.center
    pantalla.blit(texto_timer, rectangulo_texto_timer)

    tamanio_fuente_banderas = int(alto_pantalla * 0.06)
    fuente_banderas = pygame.font.SysFont("Arial", tamanio_fuente_banderas)
    texto_banderas = fuente_banderas.render(f"Banderas: {banderas_colocadas}/{minas}", True, (255,0,0))
    rectangulo_para_texto_banderas = texto_banderas.get_rect()
    rectangulo_para_texto_banderas.center = rectangulo_banderas.center
    pantalla.blit(texto_banderas, rectangulo_para_texto_banderas)

def preparar_tablero_primer_click(matriz_oculta:list[list], fila:int, col:int, filas:int, columnas:int, minas:int)->list:
    """
    Esta función permite preparar el tablero inicializando la matriz con sus filas y columnas respectivas, colocando las minas.
    
    Recibe:
        matriz_oculta (list[list]): matriz 
        fila (int): posición del clic obtenida en la función localizar_posicion_click.
        col (int): posición del clic obtenida en la función localizar_posicion_click.
        filas (int): ancho de la matriz, según dificultad.
        columnas (int): alto de la matriz, según dificultad.
        minas (int): cantidad de minas a colocar, según la dificultad.
    
    Retorna:
        list: matriz oculta según caracteristicas.
    
    """
    
    while True:
        matriz_oculta = inicializar_matriz(filas, columnas, 0)
        generar_minas(matriz_oculta, minas)
        asignar_contadores(matriz_oculta)
        if matriz_oculta[fila][col] == 0:
            break
    return matriz_oculta


def insertar_iconos_al_buscaminas(ruta:str, ancho:int, alto:int) -> pygame.Surface:
    """
    Esta función permite insertar los iconos al buscaminas.
    
    Recibe:
        ruta (str): ruta del icono a insertar.
        ancho (int): ancho a escalar el icono.
        alto (int): alto a escalar el icono.
    
    Retorna:
        pygame.Surface: icono insertado según ancho y alto.
    
    """
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen

def inicializar_matriz(filas:int, columnas:int, caracter_a_rellenar:int)->list:
    """
    Esta función permite crear una matriz e inicializarla con 0.
    
    Recibe:
        filas (int): cantidad de filas que va a tener la matriz.
        columnas (int): cantidad de columnas que va a tener la matriz.
        caracter_a_rellenar (int): caracter a rellenar en esa matriz.
    
    Retorna:
        list: matriz inicializada con 0.
    
    """
    matriz = []

    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(caracter_a_rellenar)
        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz:list[list])->None:
    """
    Esta función permite imprimir la matriz que recibimos por parametro.
    
    Recibe:
        matriz (list[list]): matriz que se va a imprimir.

    """

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def generar_minas(tablero:list[list], cantidad_minas:int, numero:int=0)->None:
    """
    Esta función permite generar las minas aleatoriamente segun el nivel de dificultad.
    
    Recibe:
        tablero (list[list]): lista simulando el tablero en donde se van a generar las minas.
        cantidad_minas (int): cantidad de minas a colocar.
        numero (int): valor minimo para el cilcado
    
    """

    while cantidad_minas > numero:
        fila = random.randint(0, len(tablero) - 1) #Elegimos una fila al azar que va de 0 hasta el ultimo elemento, por eso el -1 para q no se pase
        columna = random.randint(0, len(tablero[0]) - 1) #Hacemos lo mismo con columnas, elegimos al azar que va de 
        # 0 hasta el ultimo elemento, por eso el -1 para q no se pase
        if tablero[fila][columna] == 0: # Cuando en la fila y columna en la que estamos parado es igual a 0 le asigno un 1
            tablero[fila][columna] = "X" # Asigno 1 a la posicion en la que haya estado parado
            cantidad_minas -= 1 # Voy descontando las cantidades de minas al colocarlas


def asignar_contadores(tablero:list[list], mina:str="X")->None:
    """
    Esta función permite asignar contadores para verifica en donde se encuentran las minas y contarlas.
    
    Recibe:
        tablero (list[list]): matriz que representa el tablero.
        mina (str, valor por defecto="X"): minas en el tablero.

    """
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == mina:
                continue
            contador = 0
            # reviso las 8 posiciones posibles, con if para no salirme
            # Arriba izquierda
            if i > 0 and j > 0 and tablero[i-1][j-1] == mina:
                contador += 1
            # Arriba
            if i > 0 and tablero[i-1][j] == mina:
                contador += 1
            # Arriba derecha
            if i > 0 and j < columnas - 1 and tablero[i-1][j+1] == mina:
                contador += 1
            # Izquierda
            if j > 0 and tablero[i][j-1] == mina:
                contador += 1
            # Derecha
            if j < columnas - 1 and tablero[i][j+1] == mina:
                contador += 1
            # Abajo izquierda
            if i < filas - 1 and j > 0 and tablero[i+1][j-1] == mina:
                contador += 1
            # Abajo
            if i < filas - 1 and tablero[i+1][j] == mina:
                contador += 1
            # Abajo derecha
            if i < filas - 1 and j < columnas - 1 and tablero[i+1][j+1] == mina:
                contador += 1

            if contador > 0:
                tablero[i][j] = contador


def dibujar_buscaminas(pantalla:pygame.Surface, filas:int, columnas:int, color_lineas:tuple, color_fondo:tuple, tamanio_celda:int, matriz_visible:list, ruta_imagen_bandera:str, ruta_imagen_mina:str, mina_explota:tuple, origen_x:int = 50, origen_y:int = 40) -> None:
    """
    Esta función permite dibujar el buscaminas.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se va a dibujar el buscaminas.
        filas (int): cantidad de filas que va a tener el buscaminas.
        columnas (int): cantidad de columnas que va a tener el buscaminas.
        color_lineas (tuple): color de lineas del buscaminas.
        color_fondo (tuple): color del fondo del buscaminas.
        tamanio_celda (int): tamaño de las celdas del buscaminas.
        matriz_visible (list): matriz visible que va a tener el buscaminas.
        ruta_imagen_bandera (str): icono de la bandera del buscaminas.
        ruta_imagen_mina (str): icono de la mina del buscaminas.
        mina_explota (tuple): tupla
        origen_x (int, valor por defecto=50): origen x del buscaminas.
        origen_y (int, valor por defecto=40): origen y del buscaminas.

    """
    tamanio_fuente = tamanio_celda // 2

    if tamanio_fuente < 12:
        tamanio_fuente = 12

    
    fuente = pygame.font.SysFont("Arial", tamanio_fuente)

    for fila in range(filas):
        for columna in range(columnas):
            x = origen_x + columna * tamanio_celda
            y = origen_y + fila * tamanio_celda
            rectangulo = pygame.Rect(x, y, tamanio_celda, tamanio_celda)
            valor_matriz = matriz_visible[fila][columna]
            
            if (fila, columna) == mina_explota:
                color_celda = (200, 0, 0)
            elif valor_matriz == " ":
                color_celda = color_fondo
            else:
                color_celda = (199,191,184)
            pygame.draw.rect(pantalla, color_celda, rectangulo)

            if valor_matriz == "F":
                pantalla.blit(ruta_imagen_bandera, (x,y))
            elif valor_matriz == "X":
                pantalla.blit(ruta_imagen_mina, (x,y))
            elif valor_matriz != " " and valor_matriz != 0:
                if valor_matriz == 1:
                    color = (0,128,0)
                elif valor_matriz == 2:
                    color = (0,0,255)
                elif valor_matriz == 3:
                    color = (255,128,0)
                elif valor_matriz == 4:
                    color = (255,0,0)
                else:
                    color = (0,0,0)
                texto = fuente.render(str(valor_matriz), True, color)
                texto_rectangulo = texto.get_rect(center=(x + tamanio_celda // 2, y + tamanio_celda // 2))
                pantalla.blit(texto, texto_rectangulo)

    for fila in range(filas + 1):
        pygame.draw.line(pantalla, color_lineas, (origen_x, origen_y + fila * tamanio_celda), (origen_x + columnas * tamanio_celda, origen_y + fila * tamanio_celda), 1)

    for columna in range(columnas + 1):
        pygame.draw.line(pantalla, color_lineas, (origen_x + columna * tamanio_celda, origen_y), (origen_x + columna * tamanio_celda, origen_y + filas * tamanio_celda), 1)



def localizar_posicion_click(evento:str, filas:int, columnas:int, tamanio_celda:int, inicio_tablero_x:int, inicio_tablero_y:int) -> int:
    """
    Esta función permite localizar el click en el tablero.
    
    Recibe:
        evento (str): evento a localizar.
        filas (int): fila.
        columnas (int): columna.
        tamanio_celda (int): tamaño de la celda.
        inicio_tablero_x (int): incio de la coordenada x del tablero.
        inicio_tablero_y (int): inicio de la coordena y del tablero.
    
    Retorna:
        int: posicion fila y columna.
    
    """
    fila_columna = None
    
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1 or evento.button == 3:
            x, y = evento.pos
            x_relativo = x - inicio_tablero_x #resta el margen que hay desde el borde de la ventana hasta donde empieza el tablero
            y_relativo = y - inicio_tablero_y
            fila = y_relativo // tamanio_celda #fila y columna de la matriz se encuentra el clic
            columna = x_relativo // tamanio_celda

            if fila >= 0 and fila < filas and columna >= 0 and columna < columnas: #clic fue dentro de los límites del tablero
                if evento.button == 1:
                    print(f"Clic en la celda [{fila}, {columna}]")

                elif evento.button == 3:
                    print(f"Clic en la celda [{fila}, {columna}] BANDERA")

                fila_columna = fila, columna
            else:
                print("Click fuera del tablero")
                
    return fila_columna


def crear_texto_timer(minutos:int, segundos:int, fuente:str, color:tuple) -> str:
    """
    Esta función permite generar el texto del timer.
    
    Recibe:
        minutos (int): tiempo.
        sugundos (int): tiempo.
        fuente (str): fuente del timer.
        color (tuple): color del timer.
    
    Retorna:
        str: texto del timer.
    
    """

    tiempo_formateado = f"{minutos:02}:{segundos:02}"
    texto = fuente.render(f"Tiempo: {tiempo_formateado}", True, color)
    
    return texto


def revelar_celdas(oculta:list[list], visible:list[list], fila:int, columna:int) -> None:
    """
    Esta función permite revelar las celdas del buscaminas.
    
    Recibe:
        oculta (list[list]): matriz oculta detras de las celdas.
        visible (list[list]): matriz que se hace visible.
        fila (int): indice de fila.
        columna (int): indice de columna.

    """
    es_valido = True

    if fila < 0 or fila >= len(oculta) or columna < 0 or columna >= len(oculta[0]):
        es_valido = False
    elif visible[fila][columna] != " ":
        es_valido = False
    elif oculta[fila][columna] == "X":
        es_valido = False
        
    if es_valido == True:
        visible[fila][columna] = oculta[fila][columna]
        if oculta[fila][columna] == 0:
            for desplazamiento_fila in range(-1, 2):  # -1, 0, 1
                for desplazamiento_columna in range(-1, 2):
                    if desplazamiento_fila != 0 or desplazamiento_columna != 0:
                        nueva_f = fila + desplazamiento_fila
                        nueva_c = columna + desplazamiento_columna
                        revelar_celdas(oculta, visible, nueva_f, nueva_c)


def revelar_tablero_final(oculta:list[list], visible:list[list]) -> None:
    """
    Esta función permite revelar el tablero final.
    
    Recibe:
        oculta (list[list]): matriz oculta.
        visible (list[list]): matriz visible.
    
    """
    for fila in range(len(oculta)):
        for columna in range(len(oculta[0])):
            if visible[fila][columna] != "F": # F es bandera
                visible[fila][columna] = oculta[fila][columna]


def obtener_accion_buscaminas(pantalla:pygame.Surface, x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla de juego.
    
    Recibe:
        pantalla: (pygame.Surface) pantalla donde se va a obtener la accion.
        x (int): coordenada horizontal en donde se hizo click.
        y (int): coordenada vertical en donde se hizo click.

    Retorna:
        str: acción a realizar según click del mouse.
    
    """
    accion = None

    posiciones = calcular_posiciones_botones_inicio_fondo(pantalla)

    if x >= posiciones["posicion_x_volver"] and x <= posiciones["posicion_x_volver"] + posiciones["ancho_boton_volver"] and y >= posiciones["posicion_y_volver"] and y <= posiciones["posicion_y_volver"] + posiciones["alto_boton_volver"]:
        accion = "Volver"

    elif x >= posiciones["posicion_x_reiniciar"] and x <= posiciones["posicion_x_reiniciar"] + posiciones["ancho_boton_reiniciar"] and y >= posiciones["posicion_y_reiniciar"] and y <= posiciones["posicion_y_reiniciar"] + posiciones["alto_boton_reiniciar"]:
        accion = "Reiniciar"
    
    return accion

################################################################################################################################
#PANTALLA GANASTE

def verificar_ganador(matriz_oculta:list[list], matriz_visible:list[list]) -> bool:
    """
    Esta función permite verificar si el usuario ganó el juego.
    
    Recibe:
        matriz_oculta (list[list]): matriz oculta del usuario.
        matriz_visible (list[list]): matriz visible del usuario.
    
    Retorna:
        bool:
            True: si ganó el juego.
            False: si no ganó el juego.
    
    """
    ganador = True
    for i in range(len(matriz_oculta)):
        for j in range(len(matriz_oculta[0])):
            if matriz_oculta[i][j] != "X" and matriz_visible[i][j] == " ":
                ganador = False
    return ganador


def calcular_posiciones_pedir_nombre(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de la caja y el texto de pedir nombre para poder redimensionarlos.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual esta la caja de texto.
    
    Retorna:
        dict: diccionanrio con claves y valores de la caja de texto.
    
    """
    tamanio = pantalla.get_size()
    ancho_pantalla = tamanio[0]
    alto_pantalla = tamanio[1]
    
    posiciones = {"posicion_x_boton_guardar": int(ancho_pantalla * 0.652),
                "posicion_y_boton_guardar": int(alto_pantalla * 0.624),
                "ancho_boton_guardar": int(ancho_pantalla * 0.196),
                "alto_boton_guardar": int(alto_pantalla * 0.187),
                "posicion_x_caja": int(ancho_pantalla * 0.528),
                "posicion_y_caja": int(alto_pantalla * 0.374),
                "ancho_caja": int(ancho_pantalla * 0.456),
                "alto_caja": int(alto_pantalla * 0.187),
                "posicion_x_titulo": int(ancho_pantalla * 0.619), 
                "posicion_y_titulo": int(alto_pantalla * 0.250)}

    return posiciones

def pedir_nombre_usuario(pantalla:pygame.Surface, colo_caja_texto:tuple, color_texto:tuple, fondo:str) -> str:
    """
    Esta función permite pedir el nombre del usuario.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se pide el nombre del usuario.
        fuente (str): tipo de letra.
        colo_caja_texto (tuple): color de la caja de texto en donde se coloca el nombre.
        color_texto (tuple): color del texto.
        fondo (str): fondo en donde se dibuja todo.
    
    Retorna:
        str: nombre del usuario.

    """
    nombre = ""
    escribiendo = True
    contador_frames = 0
    
    posiciones = calcular_posiciones_pedir_nombre(pantalla)
    
    texto_base = "Ingresá tu nombre:"
    ancho_maximo = posiciones["ancho_caja"]
    tamanio_fuente = 60  # tamaño inicial grande
    
    while True:
        fuente_titulo = pygame.font.SysFont("Arial", tamanio_fuente)
        texto_titulo = fuente_titulo.render(texto_base, True, (255, 255, 255))
        if texto_titulo.get_width() <= ancho_maximo or tamanio_fuente <= 10:
            break
        tamanio_fuente -= 1

    alto_texto = texto_titulo.get_height()
    pos_y_texto = posiciones["posicion_y_caja"] - alto_texto - 10  # 10 px margen arriba del rectángulo

    while escribiendo == True:
        contador_frames += 1
        mostrar_cursor = (contador_frames // 30) % 2 == 0 
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre.strip():
                    escribiendo = False
                # si presiona enter, deja de escribir
                # simula borrar, letra por letra desde el ultimo caracter
                if evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 12:
                    nombre += evento.unicode #convierte las teclas en str
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                accion = obtener_accion_pantalla_fin_del_juego(pantalla, x, y)
                if accion == "Guardar" and nombre.strip():
                    escribiendo = False


        pantalla.blit(fondo, (0,0))
        pantalla.blit(texto_titulo, (posiciones["posicion_x_caja"], pos_y_texto))

        caja_texto = pygame.Rect(posiciones["posicion_x_caja"], posiciones["posicion_y_caja"], posiciones["ancho_caja"], posiciones["alto_caja"])
        pygame.draw.rect(pantalla, colo_caja_texto, caja_texto)

        # Crear fuente con tamaño proporcional al alto de la caja o fijo
        alto_fuente = int(posiciones["alto_caja"] * 0.6)  # por ejemplo 60% del alto de la caja
        fuente_nombre = pygame.font.SysFont("Arial", alto_fuente)
        texto_nombre = fuente_nombre.render(nombre, True, color_texto)
        pantalla.blit(texto_nombre, (posiciones["posicion_x_caja"] + 10, posiciones["posicion_y_caja"] + 10))

        dibujar_boton(pantalla, posiciones["posicion_x_boton_guardar"], posiciones["posicion_y_boton_guardar"], posiciones["ancho_boton_guardar"], posiciones["alto_boton_guardar"], "Guardar", (200,200,200), (0,0,0))

        if mostrar_cursor:
            texto_con_cursor = nombre + '|'
        else:
            texto_con_cursor = nombre
        texto_nombre = fuente_nombre.render(texto_con_cursor, True, color_texto)
        pantalla.blit(texto_nombre, (posiciones["posicion_x_caja"] + 10, posiciones["posicion_y_caja"] + 10))
        
        pygame.display.flip()

    return nombre.strip()


def calcular_posiciones_fin_de_juego(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los elementos de la pantalla de fin del juego para poder redimensionarlos .
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual están los elementos.
    
    Retorna:
        dict: diccionario con claves y valores de los elementos.
    
    """
    
    tamanio = pantalla.get_size()
    ancho_pantalla = tamanio[0]
    alto_pantalla = tamanio[1]
    
    posiciones = {"x_texto_puntaje": int(ancho_pantalla * 0.4),
                "y_texto_puntaje": int(alto_pantalla * 0.2),
                "posicion_x_boton_guardar_guardar": int(ancho_pantalla * 0.6),
                "posicion_y_boton_guardar_guardar": int(alto_pantalla * 0.6),
                "ancho_boton_guardar": int(ancho_pantalla * 0.25),
                "alto_boton_guardar": int(alto_pantalla * 0.15)}
    
    return posiciones

def obtener_accion_pantalla_fin_del_juego(pantalla:pygame.Surface, x:int, y:int) -> str:
    """
    Esta función permite obtener la accion de la pantalla del fin del jeugo.
    
    Recibe:
        pantalla (pygame.Surface): pantalla de la cual se va a obtener la accion.
        x (int): coordenada x.
        y (int): coordenada y-.
    
    Retorna:
        str: accion a realizar.
    
    """
    accion = None

    posiciones = calcular_posiciones_pedir_nombre(pantalla)

    posicion_x_boton_guardar = posiciones["posicion_x_boton_guardar"]
    posicion_y_boton_guardar = posiciones["posicion_y_boton_guardar"]
    ancho_boton_guardar = posiciones["ancho_boton_guardar"]
    alto_boton_guardar = posiciones["alto_boton_guardar"]

    if x >= posicion_x_boton_guardar and x <= posicion_x_boton_guardar + ancho_boton_guardar and y >= posicion_y_boton_guardar and y <= posicion_y_boton_guardar + alto_boton_guardar:
        accion = "Guardar"
    return accion


def calcular_puntaje(dificultad:str, total_segundos:int, banderas_colocadas:int, minas:int, fue_ganador:bool, maximo_puntaje_tiempo:int=200) -> int:
    """
    Esta función permite calcular el puntaje final del usuario.
    
    Recibe:
        dificultad (str): dificultad con la cual el usuario jugó.
        total_segundos (int): tiempo en segundos que tardó en ganar.
        banderas_colocadas (int): cantidad de banderas que colocó.
        minas (int): cantidad total de minas que había en el tablero.
        fue_ganador (bool): si el usuario fue ganador (por defecto seria True, no se calcula puntaje si se pierde)
        maximo_puntaje_tiempo (int, valor por defecto=200)
    
    Retorna:
        int: puntaje calculado.
    
    """
    if dificultad == "Facil":
        base = 100
    elif dificultad == "Medio":
        base = 250
    elif dificultad == "Dificil":
        base = 500
    else:
        base = 0

    # Calcular eficiencia banderas (entre 0 y 1)
    if minas > 0:
        proporcion_banderas = banderas_colocadas / minas
    else:
        proporcion_banderas = 0
    
    # Evitamos valores negativos y limitamos las banderas
    if proporcion_banderas < 0:
        proporcion_banderas = 0
    elif proporcion_banderas > 1:
        proporcion_banderas = 1
    
    eficiencia_banderas = proporcion_banderas * 50

    # Puntaje tiempo: 200 - tiempo, no negativo
    puntaje_tiempo = maximo_puntaje_tiempo - total_segundos
    if puntaje_tiempo < 0:
        puntaje_tiempo = 0
    
    # Calcular puntaje final según si ganó
    if fue_ganador == True:
        bonificacion = 300
        puntaje = base + eficiencia_banderas + puntaje_tiempo + bonificacion
    else:
        penalizacion = 0.5
        puntaje = (base + eficiencia_banderas + puntaje_tiempo) * penalizacion
    # No devolver puntaje negativo
    if puntaje < 0:
        puntaje = 0
    
    resultado = int(puntaje) #casteo a entero

    return resultado


def guardar_puntaje(nombre:str, puntaje:int, ruta:str="BUSCAMINAS_PYGAME/todo_pygame/puntaje.csv"):
    """
    Esta función permite guardar el puntaje en un archivo CSV.
    
    Recibe:
        nombre (str): nombre del usuario a guardar.
        puntaje (int): puntaje del usuario a guardar.
        ruta (str, valor por defecto="BUSCAMINAS_PYGAME/todo_pygame/puntaje.csv"): ruta del archivo CSV en la cual se guardan los puntajes.
    
    """

    texto_nombre = str(nombre)
    texto_puntaje = str(puntaje)

    #la línea en formato CSV (separado por comas)
    linea = texto_nombre + "," + texto_puntaje + "\n"

    with open(ruta, 'a') as archivo:
        archivo.write(linea)

###########################################################################################################################
#PUNTAJES

def calcular_posiciones_pantalla_puntajes(pantalla: pygame.Surface) -> dict:
    """
    Esta función permite calcular las posiciones de los elementos de la pantalla de puntajes para poder redimensionarlos.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se van a redimensionar los elementos.
    
    Retorna:
        dict: diccionario con claves y valores de esos elementos.
    
    """
    tamanio = pantalla.get_size()
    ancho = tamanio[0]
    alto = tamanio[1]
    
    posiciones = {"columna_x_nombre": int(ancho * 0.489),
                "columna_x_puntaje": int(ancho * 0.978),
                "y_primera_fila": int(alto * 0.212),
                "espaciado": int(alto * 0.062),
                "posicion_x_boton_guardar_volver": int(ancho * 0.782),
                "posicion_y_boton_guardar_volver": int(alto * 0.843),
                "ancho_boton_volver": int(ancho * 0.130),
                "alto_boton_volver": int(alto * 0.125)}
    
    return posiciones

#chusmea esto
def ordenar_descendentemente_los_puntajes(filas:list[list]) -> None:
    """
    Esta función permite ordenar los puntajes de mayor a menor.
    
    Recibe:
        filas (list[list]): filas

    """
    cantidad = len(filas)
    for i in range(cantidad):
        for j in range(0, cantidad - i - 1):
            if int(filas[j][1]) < int(filas[j + 1][1]):
                auxiliar = filas[j]
                filas[j] = filas[j + 1]
                filas[j + 1] = auxiliar


def mostrar_pantalla_de_puntajes(pantalla:pygame.Surface, ruta_imagen:str, ruta_puntajes:str, fuente:str):
    """
    Esta función permite mostrar la pantalla de puntajes, leyendo los datos desde el CSV.
    
    Recibe:
        pantalla (pygame.Surface): pantalla en la cual se va a mostrar la pantalla de puntajes.
        ruta_imagen (str): ruta de la imagen del fondo de la pantalla de puntajes.
        ruta_puntajes (str): ruta del archivo CSV.
        fuente (str): fuente de la letra.
    """

    posiciones = calcular_posiciones_pantalla_puntajes(pantalla)
    
    imagen_puntajes = pygame.image.load(ruta_imagen)
    imagen_puntajes = pygame.transform.scale(imagen_puntajes, pantalla.get_size())
    pantalla.blit(imagen_puntajes, (0, 0))

    dibujar_boton(pantalla, posiciones["posicion_x_boton_guardar_volver"], posiciones["posicion_y_boton_guardar_volver"], posiciones["ancho_boton_volver"], posiciones["alto_boton_volver"], "Volver", (55, 41, 22), (156, 106, 69))

    if fuente == None:
        fuente = pygame.font.SysFont("Arial", 30)

    # lee archivo de puntajes
    filas = []

    with open(ruta_puntajes, mode='r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue

            partes = linea.split(",")
            if len(partes) == 2:
                nombre = partes[0].strip()
                puntaje = partes[1].strip()
                filas.append((nombre, puntaje))
                    
    ordenar_descendentemente_los_puntajes(filas)

    filas = filas[:10]

    y = posiciones["y_primera_fila"]
    for i in range(len(filas)):
        puesto = i + 1
        nombre = filas[i][0]
        puntaje = filas[i][1]

        nombre_mostrado = str(puesto) + ". " + nombre
        ancho_nombre = fuente.size(nombre_mostrado)[0]
        ancho_puntaje = fuente.size(puntaje)[0]
        ancho_punto = fuente.size(".")[0]

        # Calculamos el espacio total disponible en píxeles entre el nombre y el puntaje
        espacio_total = posiciones["columna_x_puntaje"] - (posiciones["columna_x_nombre"] + ancho_nombre) - ancho_puntaje
        cantidad_puntos = 2
        if espacio_total > 0:
            cantidad_puntos = espacio_total // ancho_punto
        
        puntos = ""
        for _ in range(cantidad_puntos):
            puntos += "."
            
        puntos = ""
        for _ in range(cantidad_puntos):
            puntos += "."

        linea = nombre_mostrado + puntos + puntaje
        superficie = fuente.render(linea, True, (0, 0, 0))
        pantalla.blit(superficie, (posiciones["columna_x_nombre"], y))
        y += posiciones["espaciado"]


def obtener_accion_pantalla_puntajes(pantalla:pygame.Surface, x:int, y:int) -> str:
    """
    Esta función permite obtener la acción del click del mouse en la pantalla de puntajes.
    
    Recibe:
        x (int): coordenada horizontal en donde se hizo click.
        y (int): coordenada vertical en donde se hizo click.
    
    Retorna:
        str: acción a realizar según click del mouse.
    
    """
    accion = None

    posiciones = calcular_posiciones_pantalla_puntajes(pantalla)

    ancho_boton_volver = posiciones["ancho_boton_volver"]
    alto_boton_volver = posiciones["alto_boton_volver"]
    posicion_horizontal_boton_volver = posiciones["posicion_x_boton_guardar_volver"]
    posicion_vertical_boton_volver = posiciones["posicion_y_boton_guardar_volver"]

    if x >= posicion_horizontal_boton_volver and x <= posicion_horizontal_boton_volver + ancho_boton_volver and y >= posicion_vertical_boton_volver and y <= posicion_vertical_boton_volver + alto_boton_volver:
        accion = "Volver"
    
    return accion