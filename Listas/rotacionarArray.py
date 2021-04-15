'''
    developed by Karen Lorhana
'''
lista = []
qtdInteiros = int(input())

for i in range(qtdInteiros):
    numeros = int(input())
    lista.append(numeros)

deslocamentos = int(input())

for i in range(deslocamentos, qtdInteiros):
    print(lista[i])
    
for j in range(qtdInteiros):
    print(lista[j])

