vendedor=input()
salFixo=float(input())
totalVendas=float(input())
comissao=totalVendas*0.15
salTotal=salFixo+comissao
print("TOTAL =", "R$","%.2f"%salTotal)