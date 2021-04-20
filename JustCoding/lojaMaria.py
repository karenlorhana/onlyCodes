'''
    developed by Karen Lorhana
'''

qtdDoces = int(input("Informe a quantidade de doces comprados: "))
doces = 0
preco = 0
indice = 0
maisBarato = 10000000

for i in range(1,qtdDoces+1):
    print("Doce ", i)
    pesoDoces = int(input("Peso (g): "))
    doces += pesoDoces
    valorDoces = float(input("Valor (R$): "))
    preco += valorDoces
    precoUnitario = (valorDoces/pesoDoces) * 1000
    print("Preço unitário: ", " R$", precoUnitario,"/kg")
    if precoUnitario < maisBarato:
        maisBarato = precoUnitario
        indice = i
print("Produto mais barato: Doce ",indice, ", R$", maisBarato,"/kg")
print("Foram comprados ",doces, "g de doce por R$", preco)