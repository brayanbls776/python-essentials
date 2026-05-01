import random

tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def display_board(board):
# La función muestra el tablero con los movimientos actuales.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |") 
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # La función solicita al jugador que ingrese su movimiento, verifica que sea válido y actualiza el tablero
    while True:
        jugada = input("Ingrese su movimiento : ")
        try:
            movimiento = int(jugada)   
            
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        if movimiento < 1 or movimiento > 9:
            print("Movimiento no válido. Intente de nuevo.")         
        else:
            # Aquí va tu lógica para marcar el tablero...
            encontrado = False
            for i in range(3):
                for j in range(3):
                    if board[i][j] == movimiento:
                        board[i][j] = "O"
                        encontrado = True            
            if encontrado:
                break
            else:
                print("Esa casilla ya está ocupada.")
              
def make_list_of_free_fields(board):
# La función crea una lista de las casillas libres en el tablero y luego la computadora elige una al azar para marcarla con "X".
    libres = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if tablero[i][j] != "X" and tablero[i][j] != "O":
                datos=(i, j)
                libres.append(datos)
    if len(libres) > 0:
        # La computadora elige una tupla al azar de la lista
        eleccion = random.choice(libres)  
        # Extraemos la fila y columna de la tupla elegida
        fila_cpu, col_cpu = eleccion
        # Marcamos el tablero ( CPU es "X")
        tablero[fila_cpu][col_cpu] = "X"
    
        print(f"La computadora eligió la casilla: {eleccion}")
    else:
        print("¡Empate! No hay más espacios libres.")          
    
def ganador(board):
# La función examina el tablero para determinar si hay un ganador. Si el jugador gana, devuelve "O". Si la computadora gana, devuelve "X". Si no hay ganador, devuelve None.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
            
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
            
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
        
    return None

print("Bienvenido al juego de Tic Tac Toe!")
display_board(tablero)
while True:
    
    enter_move(tablero)
    resultado =ganador(tablero)
    if resultado == "O":
        print("¡Felicidades! Has ganado.")
        break

    make_list_of_free_fields(tablero)
    display_board(tablero)
    resultado = ganador(tablero)
    if resultado == "X":
        print("La computadora ha ganado. ¡Inténtalo de nuevo!")
        break
