'''
    developed by Karen Lorhana
'''
lista = []
qtdInteiros = int(input())

for j in range(qtdInteiros):
    lista.append(int(input()))

deslocamentos = int(input())

for i in range(qtdInteiros):
    if i + deslocamentos < qtdInteiros:
        print(lista[i+deslocamentos])
    else:
        print(lista[(i+deslocamentos)-qtdInteiros]) 