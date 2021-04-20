dia = str(input())
valorProduto = float(input())
opcaoProduto = str(input())
nomeProduto = str(input())
valorN = float(0)

if (dia == "seg" or dia == "ter" or dia == "qua"):
    if (opcaoProduto == "ouro"):
        valorN = valorProduto / 2
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)
    else:
        valorN = 2 * valorProduto
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)

elif (dia == "qui" or dia == "sex"):
    if (10 <= valorProduto <= 100):
        valorN = valorProduto / 3
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)
    else:
        valorN = 2 * valorProduto
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)

elif (dia == "sab"):
    if (opcaoProduto == "prata"):
        valorN = 3 * valorProduto
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)
    else:
        valorN = 2 * valorProduto
        print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)

else:
    valorN = 2 * valorProduto
    print("O preco do produto", nomeProduto, "no dia", dia, "eh", "%.2f" % valorN)