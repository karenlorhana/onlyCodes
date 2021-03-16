numero = int(input())
i = 1
n = 0

if numero < 3:
    print("Falso")
else:
    while n < numero:
        n = i*(i+1)*(i+2)
        if n != numero:
            i +=1

    if n == numero:
        print('%d * %d * %d = %d \nVerdadeiro'%(i, (i+1), (1+2), n))
    else:
        print("Falso")