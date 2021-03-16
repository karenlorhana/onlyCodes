''' 
    Developed by Karen Lorhana
'''

qtdPagamentoCartao = 0 
qtdPagamentoVista = 0
somaPagamentoVista = 0 
somaPagamentoCartao = 0
somaPagamento = 0
menorIdade = 10000
maiorCompra = 0
mediaVista = 0

while True:
        idade = int(input())
        valorCompra = float(input())
        tipoPagamento = str(input()).upper() #C no cartão; A à vista
        continua = str(input()).upper() #S ou N
        
        if tipoPagamento == "C":
            somaPagamentoCartao += valorCompra
            qtdPagamentoCartao += 1
            
        elif tipoPagamento == "V":
            somaPagamentoVista += valorCompra
            qtdPagamentoVista += 1
        somaCompras = somaPagamentoVista + somaPagamentoCartao
        somaPagamento = qtdPagamentoVista + qtdPagamentoCartao
        
        if idade < menorIdade:
            menorIdade = idade
        if valorCompra > maiorCompra:
            maiorCompra = valorCompra
        if tipoPagamento == "V":
            
            mediaVista = somaPagamentoVista / qtdPagamentoVista
    
        if continua == "N":
             break

print(somaPagamento)
if somaPagamentoVista == 0:
    print(0)
else:
    print("%.2f"%somaPagamentoVista)
if somaPagamentoCartao == 0:
    print(0)
else:
    print("%.2f"%somaPagamentoCartao)
print(menorIdade)
print("%.2f"%maiorCompra)
if mediaVista == 0:
    print(0)
else:
    print(mediaVista)
