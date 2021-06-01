''''
    developed by Karen Lorhana
'''
matriz = [[1, 11, 111], 
    [2, 22, 222],
    [3, 33, 333]]



#forma 1 de se fazer:

#forma 2 de se fazer:

for i in range(3): #diagonal principal
   print(matriz[i][i], end=" ")

'''  
for i in range(2,-1,-1): #diagonal secundaria
    matriz.reverse()
    print(matriz[i][i], end=" ")
'''