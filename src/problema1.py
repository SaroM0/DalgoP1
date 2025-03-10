# ------------------------------------------------------------------------------
# ProblemaP1.py
#
# Autores:
# Santiago Rodriguez Mora - 202110332
# Angel...
#
# Este script resuelve la primera parte del "Juego del Algormar".
# Lee casos de prueba desde la entrada estándar y produce la suma mínima posible
# de los primeros j jugadores tras realizar como máximo m intercambios adyacentes.
#
# Formato de entrada:
#   - La primera línea contiene T (el número de casos de prueba).
#   - Cada uno de los T casos de prueba se describe en una sola línea:
#       n j m seguido de n enteros que representan el peso energético de cada jugador.
#
# Formato de salida:
#   - Para cada caso de prueba, se imprime en una sola línea la suma mínima
#     de los primeros j jugadores después de realizar, como máximo, m intercambios.
#
# Restricciones (según el enunciado):
#   1 <= n <= 10
#   1 <= j <= n
#   1 <= m <= 10
#   1 <= q_i <= 10
# ------------------------------------------------------------------------------

import sys

def solve():
    # Leer el número de casos de prueba
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        # Leer la línea correspondiente a un caso de prueba
        data_line = list(map(int, sys.stdin.readline().strip().split()))
        
        # Extraer n, j, m
        n = data_line[0]
        j = data_line[1]
        m = data_line[2]
        
        # Extraer el arreglo de pesos energéticos
        energies = data_line[3:]
        
        # Enfoque codicioso (greedy):
        # Para cada posición i en [0..j-1], traer el elemento más pequeño posible
        # desde el rango [i..i+m] (limitado por n-1) hasta la posición i
        # mediante intercambios adyacentes.
        
        for i in range(j):
            if m <= 0:
                # Si ya no hay intercambios disponibles, se sale del bucle
                break
            
            # Determinar el índice límite en el que aún es posible intercambiar
            limit_index = min(n - 1, i + m)
            
            # Encontrar el índice del elemento más pequeño en el subarreglo [i..limit_index]
            min_index = i
            min_value = energies[i]
            
            for k in range(i + 1, limit_index + 1):
                if energies[k] < min_value:
                    min_value = energies[k]
                    min_index = k
            
            # Calcular la distancia para mover min_index hasta i
            distance = min_index - i
            
            # Realizar los intercambios adyacentes
            while min_index > i:
                # Intercambiar con el elemento anterior
                energies[min_index], energies[min_index - 1] = energies[min_index - 1], energies[min_index]
                min_index -= 1
                # Disminuir el contador de intercambios disponibles
                m -= 1
                if m <= 0:
                    break
        
        # Calcular la suma de los primeros j elementos resultantes
        result = sum(energies[:j])
        
        # Imprimir la suma mínima para este caso
        print(result)

# Para ejecutar la función solve() al ejecutar el script directamente:
if __name__ == "__main__":
    solve()
