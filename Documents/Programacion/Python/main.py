def matriz_vacia(filas, columnas):
    #matriz creada para llevar el conteo de las casillas visitadas
    matriz = []
    for f in range(filas):
        fila_nueva = []
        for c in range(columnas):
            fila_nueva.append(False)
        matriz.append(fila_nueva)
    return matriz

def girar_derecha(direccion_actual):
    if direccion_actual == "DERECHA":
        return "ABAJO"
    elif direccion_actual == "ABAJO":
        return "IZQUIERDA"
    elif direccion_actual == "IZQUIERDA":
        return "ARRIBA"
    elif direccion_actual == "ARRIBA":
        return "DERECHA"

def calcular_siguiente_paso(fila_actual, col_actual, direccion):
    nueva_fila = fila_actual
    nueva_col = col_actual
    
    if direccion == "DERECHA":
        nueva_col = nueva_col + 1
    elif direccion == "ABAJO":
        nueva_fila = nueva_fila + 1
    elif direccion == "IZQUIERDA":
        nueva_col = nueva_col - 1
    elif direccion == "ARRIBA":
        nueva_fila = nueva_fila - 1
        
    return (nueva_fila, nueva_col)

# Funcion de validación 
def validacion(fila, col, max_filas, max_cols):
    if fila < 0 or fila >= max_filas:
        return False
    if col < 0 or col >= max_cols:
        return False
    
    return True

def movimiento_valido(fila, col, max_filas, max_cols, visitados):
    if not validacion(fila, col, max_filas, max_cols):
        return False
    
    if visitados[fila][col] == True:
        return False
        
    return True

def direccion_final(N, M):
    # validación inicial de dimensiones
    if N <= 0 or M <= 0:
        return "Dimensiones no válidas"

    fila_actual = 0
    col_actual = 0
    direccion_actual = "DERECHA" # empezamos hacia la derecha 
    
    visitados = matriz_vacia(N, M)
    
    total_casillas = N * M
    casillas_visitadas_contador = 0
    
    # bucle principal, el cual se ejecuta si no hemos visitado todas las casillas
    while casillas_visitadas_contador < total_casillas:
        
        # revisamos la casilla actual
        if visitados[fila_actual][col_actual] == False:
            visitados[fila_actual][col_actual] = True
            casillas_visitadas_contador = casillas_visitadas_contador + 1
        # si ya se visitaron todas las casillas, salimos del bucle
        if casillas_visitadas_contador == total_casillas:
            break

        # primero, calculamos a donde iríamos si seguimos recto
        (siguiente_fila, siguiente_col) = calcular_siguiente_paso(fila_actual, col_actual, direccion_actual)
        
        # comprobamos si es valido ese movimiento
        if movimiento_valido(siguiente_fila, siguiente_col, N, M, visitados):
            fila_actual = siguiente_fila
            col_actual = siguiente_col
            
        else:
            direccion_actual = girar_derecha(direccion_actual)
            (siguiente_fila_despues_giro, siguiente_col_despues_giro) = calcular_siguiente_paso(fila_actual, col_actual, direccion_actual)
            
            fila_actual = siguiente_fila_despues_giro
            col_actual = siguiente_col_despues_giro

    return direccion_actual

#ejecucion del programa en el cual solicitar al usuario que ingrese los valores de prueba
if __name__ == "__main__":

    print("Programa para determinar la dirección final de un recorrido en espiral en una matriz NxM.")

    while True:
        try:
            N = int(input("Ingrese el número de filas (N): "))
            M = int(input("Ingrese el número de columnas (M): "))

            resultado = direccion_final(N, M)

            print(f"\nPara una matriz de {N}x{M}, la dirección final es: {resultado}")

        except ValueError:
            print("\n¡Error! Por favor, ingrese números enteros válidos para las dimensiones.")
            continuar = input("¿Desea intentar de nuevo? (s/n): ").strip().lower()
            if continuar not in ("s", "si"):
                print("Saliendo.")
                break
            else:
                continue

        # preguntar si desea calcular otra matriz
        continuar = input("\n¿Desea calcular otra matriz? (s/n): ").strip().lower()
        if continuar not in ("s", "si"):
            print("Saliendo.")
            break