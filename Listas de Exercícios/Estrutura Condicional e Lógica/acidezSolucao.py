valorPh = float(input())

if(valorPh ==  0 or valorPh < 7):
    print("Acida")
elif(valorPh > 7 or valorPh == 14):
    print("Basica")
else:
    print("Neutra")