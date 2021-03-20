''' 
    Developed by Karen Lorhana
'''

num1 = int(input())
num2 = int(input())
soma = 0

if num2 <= num1:
    print("Digite um valor maior que o primeiro!")
    num2 = int(input())
    while num2 <= num1:
        print("Digite um valor maior que o primeiro!")
        num2 = int(input())
for i in range(num1,num2+1):
    qtdDivisoresPrimos = 0
    for x in range(1,i+1):
        if i % x == 0:
            qtdDivisoresPrimos += 1
    if qtdDivisoresPrimos == 2:
        soma += i
if soma != 0:
    print(soma)
else:
    print("Sem números primos no intervalo informado.")
