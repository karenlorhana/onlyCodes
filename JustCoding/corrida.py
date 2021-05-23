def calcular_nivel(velocidade):
    maior = maximo(velocidade)
    for i in (velocidade):
        if maior < 10:
            return 1
        elif maior >= 10 and maior < 20:
            return 2
        elif maior >= 20:
            return 3
    return calcular_nivel

def maximo(velocidade):
    maior = 0
    for i in (velocidade):
        if i > maior:
            maior = i
    return maior

while True:
    qtdLesmas = int(input())
    if qtdLesmas != 0:
        velocidade = input().split()
        velocidade = list(map(int, velocidade))
        print(calcular_nivel(velocidade))
    else:
        break




