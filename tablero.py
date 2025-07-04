import random

def inicializar_matriz(filas:int, columnas:int, caracter_a_rellenar:int)->list[list]:
    """Documentacion:
    creamos una matriz y la inicializamos con los 0 (ceros)"""
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(caracter_a_rellenar)
        matriz.append(fila)

    return matriz #La retorno unicamente porque la estoy creando dentro de la funcion, de lo contrario no haria falta ya que es mutable


def mostrar_matriz(matriz)->None:
    """Documentacion: 
    Solo imprimimos la matriz que recibimos por parametro"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def generar_minas(tablero:list[list], cant_minas:int)->None:
    """
    Documentacion:
    Recibimos una lista simulando el tablero, y la cantidad de minas a colocar
    en lugares aleatorios 
    """
    while cant_minas > 0:
        fila = random.randint(0, len(tablero) - 1) #Elegimos una fila al azar que va de 0 hasta el ultimo elemento, por eso el -1 para q no se pase
        columna = random.randint(0, len(tablero[0]) - 1) #Hacemos lo mismo con columnas, elegimos al azar que va de 
        # 0 hasta el ultimo elemento, por eso el -1 para q no se pase
        if tablero[fila][columna] == 0: # Cuando en la fila y columna en la que estamos parado es igual a 0 le asigno un 1
            tablero[fila][columna] = "X" # Asigno 1 a la posicion en la que haya estado parado
            cant_minas -= 1 # Voy descontando las cantidades de minas al colocarlas

def asignar_contadores(tablero:list[list], mina:str="X")->None:
    """Documentacion:
    recibimos la matriz que representa nuestro tablero, y como parametro opcional
    le asignamos una mina como X para luego verificar donde se encuentran las X 
    y poder contarlas"""
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == mina:
                continue
            contador = 0
            # Reviso manualmente las 8 posiciones posibles, con if para no salirme
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

# Código principal
matriz = inicializar_matriz(8, 8, 0)
generar_minas(matriz, 10)
asignar_contadores(matriz)
mostrar_matriz(matriz)