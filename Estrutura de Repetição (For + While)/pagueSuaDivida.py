valorDivida = int(input())
valorPago = int(input())

while valorDivida > 0:
    print("(antes) {}".format(valorDivida))
    if valorDivida <= valorPago:
        valorDivida = 0
    else:
        valorDivida -= valorPago
    print("(depois) {}".format(valorDivida))