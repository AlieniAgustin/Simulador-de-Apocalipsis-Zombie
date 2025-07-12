import numpy as np

def initialize_matrix(n):
    options = list(range(0, 4)) #4 excluido
    probabilities = [0.15, 0.4, 0.3, 0.15] # zona segura - zombie - humano - hospital
    matrix = np.random.choice(options, size = (n, n), replace = True, p = probabilities)
    return matrix

def infect_humans(matrix):
    pass 

def main():
    n = int(input("Ingresa el tamano que tendra la matriz cuadrada: "))
    matrix = initialize_matrix(n)
    
    for i in range(n+1):
        infect_humans(matrix)




if __name__ == "__main__":
    main()
