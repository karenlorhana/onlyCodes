def elementoJogo():
    elementos = []
    for i in range(10):
        elementos.append(str(input()))
    return elementos

def elementoVerifica():
    resultado = []
    for i in range(0,10,2):
        if jogo[i] != jogo[i+1]:
            if jogo[i] == "papel":
                if jogo[i+1] == "tesoura":
                    resultado.append(1)
                else:
                    resultado.append(0)
            elif jogo[i] == "pedra" :
                if jogo[i+1] == "papel":
                    resultado.append(1)
                else:
                    resultado.append(0)
            else:
                if jogo[i+1] == "pedra":
                    resultado.append(1)
                else:
                    resultado.append(0)
        else:
            resultado.append(2)
    return resultado
    
while True:
    jogo = elementoJogo()
    result = elementoVerifica()
    if result.count(0) < result.count(1):
        print("MIGUEL")
        break
    elif result.count(0) > result.count(1):
        print("MARIA RITA")
        break