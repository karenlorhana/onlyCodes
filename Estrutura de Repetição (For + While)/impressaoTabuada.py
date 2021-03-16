''' 
    Developed by Karen Lorhana
'''

while  True:
    num1 = int(input())
    if num1 < 1 or num1 > 9:
        print("Insira um número inicial entre 1 e 9")
    else:
        break

while True:
    num2 = int(input())
    if num2 < 1 or num2 > 9:
        print("Insira um número final entre 1 e 9")
    else:
        break

if num1 > num2:
    print("Nenhuma tabuada nesse intervalo")

for x in range (num1, num2+1):
    for i in range(1, 10):
        print(x, "x", i, "=", x*i)
    print()