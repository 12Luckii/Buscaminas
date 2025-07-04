#Iniciales
NOMBRE_JUEGO = "Buscaminas"
ANCHO_PANTALLA = 1534 #1534
ALTO_PANTALLA = 801 #801

#Rutas
RUTA_ICONO_VENTANITA = "BUSCAMINAS_PYGAME/Imagenes/icono_ventanita.png"
RUTA_IMAGEN_INICIO = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_inicio.png"
RUTA_IMAGEN_SELECCION_DE_NIVELES = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_niveles.png"
RUTA_IMAGEN_PUNTAJES = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_puntajes.png"
RUTA_IMAGEN_GANASTE = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_ganaste.png"
RUTA_IMAGEN_PERDISTE = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_perdiste.png"
RUTA_IMAGEN_BANDERA = "BUSCAMINAS_PYGAME/Imagenes/bandera.png"
RUTA_IMAGEN_MINA = "BUSCAMINAS_PYGAME/Imagenes/mina.png"
RUTA_MUSICA_VICTORIA = "BUSCAMINAS_PYGAME/Musica/musica_victoria.mp3"
RUTA_MUSICA_DERROTA = "BUSCAMINAS_PYGAME/Musica/musica_derrota.mp3"
RUTA_ARCHIVO_PUNTAJES = "BUSCAMINAS_PYGAME/todo_pygame/puntaje.csv"

RUTA_MUSICA_JUEGO = "BUSCAMINAS_PYGAME/Musica/musica_juego.mp3"
RUTA_ICONO_MUSICA_ON = "BUSCAMINAS_PYGAME/Imagenes/sonido_on.png"
RUTA_ICONO_MUSICA_OFF = "BUSCAMINAS_PYGAME/Imagenes/sonido_off.png"

#Transicion
TIEMPO_DE_TRANSICION = 5000

#Buscaminas
COLOR_LINEAS_BUSCAMINAS = (0,0,0)
COLOR_FONDO_BUSCAMINAS = (220,220,220)
COLOR_DEL_TIMER = (0,0,255)
FUENTE_DEL_TIMER = "Arial"
TAMANIO_FUENTE_TIMER = 50

#Puntajes
FUENTE_PUNTAJES = "Arial"
TAMANIO_FUENTE_PUNTAJES = 60
FUENTE_PUNTITOS_PUNTAJES = "Arial"
TAMANIO_FUENTE_PUNTITOS = 32

#Pedir nombre
COLO_CAJA_TEXTO_PEDIR_NOMBRE = (255,255,255)
COLOR_TEXTO_CAJA_PEDIR_NOMBRE = (0,0,0)


matriz_oculta = None
matriz_visible = None
primer_click_realizado = False
banderas_colocadas = 0
perdi = False
gane = False
tiempo_transicion = 0
pantalla_fin = False
fue_ganador = False
tiempo_inicializado = False
minutos = 0
segundos = 0
filas = 0
columnas = 0
minas = 0
tamanio_celda = 0
nombre_usuario = ""
nombre_completo = False
mina_explota = None
resoluciones = [(1534, 801), (1300, 700), (1100, 600)]
indice_resolucion_actual = 0
musica_activa = True
click_icono_sonido = None

origen_x = int(ANCHO_PANTALLA * 0.05)  # 5% del ancho total
origen_y = int(ALTO_PANTALLA * 0.05)   # 5% del alto total

pantalla_actual = "Inicio"
corriendo_juego = True