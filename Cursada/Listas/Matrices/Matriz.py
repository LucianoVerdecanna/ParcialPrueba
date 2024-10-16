matrix = [[2, 4, 5, 8], [6, 3, 1, 9]]

print(matrix)
def visualizar_matriz(i,j):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end= " ")
        print("")


print(visualizar_matriz(2,4))

