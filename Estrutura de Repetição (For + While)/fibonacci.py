''' 
    Developed by Karen Lorhana
'''

n = int(input())
while (n != 0):
    if(n == 1):
        print("0")
    elif(n > 1):
        fibonacciUm = 0
        fibonacciDois = 1
        print('{} {}'.format(fibonacciUm,fibonacciDois),end='')
        x = 3
        while(x <= n):
            fibonacciFinal = fibonacciUm + fibonacciDois
            print(' {}'.format(fibonacciFinal),end='')
            fibonacciUm = fibonacciDois
            fibonacciDois = fibonacciFinal
            x += 1
        print("")
    n = int(input())