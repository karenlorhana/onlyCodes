def validarData(data):
    data = data.split("/")
    valido = False
    dia = (str(data[0]))
    mes = str(data[1])
    ano = str(data[2])
    if(int(dia) >= 1 and int(dia) <= 31):
        valido = True 
    else:
        valido = False
    if(int(mes) >= 1 and int(mes) <= 12):
        valido = True
    else:
        valido = False
    if (int(mes) == 2 and int(dia) > 28):
        valido = False
    else:
        valido = True
    if (int(ano) > 0):
        valido = True
    else:
        valido = False

    return valido

def calcularDias(data1, data2):
    if(validarData(data1) == False or validarData(data2) == False):
        return -1

    data1 = data1.split("/")
    dia1 = data1[0]
    mes1 = data1[1]
    ano1 = data1[2]

    data2 = data2.split("/")
    dia2 = data2[0]
    mes2 = data2[1]
    ano2 = data2[2]

    diaFinal = int(dia2) - int(dia1)
    mesFinal = int(mes2) - int(mes1)
    anoFinal = int(ano2) - int(ano1)
    dataFinal = (diaFinal)
    if mesFinal != 0:
        mesFinal *= 30
        dataFinal += mesFinal
    if anoFinal != 0:
        anoFinal *= 360
        dataFinal += anoFinal
    return dataFinal

def calcularValorFinal(valorDiaria, diasAlocados,  rodadosKm):
    
    valorFinal = ((valorDiaria * diasAlocados) + (0.30 * rodadosKm))
    return valorFinal

def validaKM(km1, km2):
    if km1 > km2 or km1 < 0 or km2 <= 0:
        return -1
    else: 
        return km2 - km1

def verificaModelo(modeloCarro):
    if modeloCarro == "b" :
        return 30.00
    elif modeloCarro == "p" :
        return 60.00

    elif modeloCarro == "i":
        return 40.00
    else:
        return -1

while True:
    modeloCarro = str(input())
    if modeloCarro != "FIM":
        dataRetirada = str(input())
        dataDevolucao = str(input())
        kmRodados = str(input()).split()
        kmRodados = list(map(int, kmRodados))

        modeloC = verificaModelo(modeloCarro)
        dataFinal = calcularDias(dataRetirada, dataDevolucao)
        kmTotal = validaKM(kmRodados[0], kmRodados[1])
        
        if modeloC == -1:
            print("Modelo de carro invalido")
        else:
            if dataFinal == -1:
                print("Data invalida")
            else:
                if kmTotal == -1:
                    print("Valores do odometro com erro")
                else:
                    valor = calcularValorFinal(modeloC, dataFinal, kmTotal)
                    print( valor )
            
    else:
        break


