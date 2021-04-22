matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for lin in range(3):
    for col in range(4):
        matriz[lin][col] = int(input())
matrizTransposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for transposta in range(4):
    matrizTransposta[transposta][0] = matriz[0][transposta]
    matrizTransposta[transposta][1] = matriz[1][transposta]
    matrizTransposta[transposta][2] = matriz[2][transposta]
print("A matriz transposta é: ", matrizTransposta)