

def baralhoIguais():
    if carta[0] == carta[1] == carta[2]:
        pontos.append(min(carta))
    baralhoMenores()

def baralhoMaiores():
    verificar = carta.copy()
    verificar.remove(min(carta))
    if verificar[0] == verificar[1] and  verificar[0] != min(carta):
        pontos.append(verificar[0]//2)
    baralho8()

    
def baralhoMenores():
    verificar = carta.copy()
    verificar.remove(max(carta))
    if verificar[0] == verificar[1] and verificar[0] != max(carta):
        pontos.append(verificar[0]//2)
    baralhoMaiores()

def baralhoCrescente():
    if carta[0]+1 == carta[1] and carta[1]+1 == carta[2]:
        pontos.append(min(carta))
    baralhoIguais() 

    
def baralho8():
    if sum(carta) == 8:
        pontos.append(8)
    
carta = input().split()
carta = list(map(int,carta))
carta.sort()
pontos = []
baralhoCrescente()
num1 = sum(pontos)

carta = input().split()
carta = list(map(int,carta))
carta.sort()
pontos = []
baralhoCrescente()
num2 = sum(pontos)

if num1 == num2:
    print(0)
elif num1 > num2:
    print(1)
else:
    print(2)