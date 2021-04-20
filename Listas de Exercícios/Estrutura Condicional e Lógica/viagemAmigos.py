qtdPessoas = int(input())
cidadeEscolhida = (input()).upper()
qtdQuartos = int(input())

if (cidadeEscolhida == "PIPA"):
    passeio = 75.00 * qtdPessoas
    if(qtdQuartos == 2):
        totalViagem = 600.00 + passeio
        valorDividido = totalViagem / qtdPessoas
        print("%.2f"%totalViagem)
        print("%.2f"%valorDividido)
    elif(qtdQuartos == 3):
        totalViagem = 900.00 + passeio
        valorDividido = totalViagem / qtdPessoas
        print("%.2f" % totalViagem)
        print("%.2f" % valorDividido)
elif (cidadeEscolhida == "FORTALEZA"):
    passeio = 60.00 * qtdPessoas
    if(qtdQuartos == 3):
        totalViagem = 950.00 + passeio
        valorDividido = totalViagem / qtdPessoas
        print("%.2f" % totalViagem)
        print("%.2f" % valorDividido)
    elif(qtdQuartos == 4):
        totalViagem = 1120.00 + passeio
        valorDividido = totalViagem / qtdPessoas
        print("%.2f" % totalViagem)
        print("%.2f" % valorDividido)