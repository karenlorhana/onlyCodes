'''
10
10 10 10 10 15 18 20 15 11 10     3
5
1 5 2 9 5          1
7 
1 9 9 1 4 5 8 6     2
'''
def calcular_nivel():
    maior = 0
    for i in (velocidade):
        if i > maior:
            maior = i
        for i in (velocidade):
            if maior < 10:
                return 1
            elif maior >= 10 and maior < 20:
                return 2
            elif maior >= 20:
                return 3
    
    return calcular_nivel()
#def maximo():
   

while True:
    qtdLesmas = int(input())
    if qtdLesmas != 0:
        velocidade = input().split()
        velocidade = list(map(int, velocidade))
        print(calcular_nivel())
    else:
        break




