import numpy as np

class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = np.empty((n,n), dtype=str)
        for i in range(n):
            for j in range(n):
                self.tablero[i][j]=' '

    def __str__(self):
        return str(self.tablero)

    def colocar_torre(self):
        if 0<self.n-1:
            for i in range(self.n):
                self.tablero[0][i]='r'
                self.tablero[1][i]='R'
        else:
            pass
        self.tablero[0][0]='R'
        self.tablero[1][0]=' '
        self.tablero[self.n-1][0]='r'
        return self.tablero

piezas = {'R': '\u265C',
            'r': '\u2656',
}

R = piezas['R']
r = piezas['r']

def pedir_numero(cond):
    n = int(input('Introduce un número para {}: '.format(cond)))
    return n

def pedir_numero1o2(cond):
    n = int(input('Introduce un número entre {}: '.format(cond)))
    while n != 1 and n != 2:
        n = int(input('Introduce un número entre {}: '.format(cond)))
    return n

def crear_tablero(n):
    tablero = np.empty((n,n), dtype=str)
    for i in range(n):
        for j in range(n):
            tablero[i][j]=' '
    return tablero


def colocar_torre(n):
    tablero = crear_tablero(n)
    if 0<n-1:
        for i in range(n):
            tablero[0][i]=r
            tablero[1][i]=R
    else:
        pass
    tablero[0][0]=R
    tablero[1][0]=' '
    tablero[n-1][0]=r
    return tablero

#detectar la posicion de una unica torre blanca
def seleccionar_torre_blanca(tablero):
    posicion = []
    n = pedir_numero("seleccionar la torre blanca")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == R:
                posicion.append([i,j])
    posicion_n = posicion[n-1]
    return posicion_n


def seleccionar_torre_negra(tablero):
    posicion = []
    n = pedir_numero("seleccionar la torre negra")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == r:
                posicion.append([i,j])
    posicion_n = posicion[n-1]
    return posicion_n

#movimiento de las torres   
def movimiento_torre_blanca(n):
    n = input('elegir el tamaño del tablero')
    tablero = colocar_torre()
    print(tablero)
    torre = seleccionar_torre_blanca(tablero)
    numero_casillas = pedir_numero("mover la torre")
    h = torre[0]
    v = torre[1]
    pos = [h, v]
    if pos[0] + numero_casillas < 8:
        if tablero[pos[0]+numero_casillas][pos[1]] == ' ':
            tablero[pos[0] + numero_casillas][pos[1]] = R
            tablero[pos[0]][pos[1]] = ' '
        else: 
            return 'Movimiento no válido'
    else:
        return 'Movimiento no válido'
    return tablero

def movimiento_torre_blanca():
    n = pedir_numero('elegir el tamaño del tablero')
    tablero = colocar_torre(n)
    print(tablero)
    torre = seleccionar_torre_blanca(tablero)
    numero_casillas = pedir_numero("mover la torre")
    h = torre[0]
    v = torre[1]
    pos = [h, v]
    if pos[0] + numero_casillas < n:
        if tablero[pos[0]+numero_casillas][pos[1]] == ' ':
            tablero[pos[0] + numero_casillas][pos[1]] = R
            tablero[pos[0]][pos[1]] = ' '
        else: 
            return 'Movimiento no válido'
    else:
        return 'Movimiento no válido'
    return tablero


def movimiento_torre_negra():
    n = pedir_numero('elegir el tamaño del tablero')
    tablero = colocar_torre(n)
    print(tablero)
    torre = seleccionar_torre_negra(tablero)
    numero_casillas = pedir_numero("mover la torre")
    h = torre[0]
    v = torre[1]
    pos = [h, v]
    if pos[0] + numero_casillas < n:
        if tablero[pos[0]+numero_casillas][pos[1]] == ' ':
            tablero[pos[0] + numero_casillas][pos[1]] = r
            tablero[pos[0]][pos[1]] = ' '
        else: 
            return 'Movimiento no válido'
    else:
        return 'Movimiento no válido'
    return tablero


if __name__ == "__main__":
    n = pedir_numero1o2("1 o 2")
    if n == 2:
        print(movimiento_torre_blanca())
        print("Blancas ganan")
    else:
        print(movimiento_torre_negra())
        print("Negras ganan")