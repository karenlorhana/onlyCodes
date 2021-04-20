escalaTemp=(input())
temperatura=float(input())
if (escalaTemp=="K"):
  if (temperatura>=0.0):
     tempCelcius=temperatura-273.15
     temperaFahrenheit= 1.8*(temperatura-273.15)+32
     print("%.2f C"%tempCelcius)
     print("%.2f F"%temperaFahrenheit)
  else:
    print("Valor de temperatura abaixo do minimo")
elif (escalaTemp=="C" and  temperatura>=-273.0):
     tempFahrenheit= 1.8*temperatura+32
     tempKelvin=temperatura+273.15
     print("%.2f F"%tempFahrenheit)
     print("%.2f K"%tempKelvin)
elif (escalaTemp=="F" and temperatura>=-459.67):
     tempCelcius=(temperatura-32)/1.8
     tempKevin=tempCelcius+273.15
     print("%.2f C"%tempCelcius)
     print("%.2f K"%tempKevin)
else:
     print("Valor de temperatura abaixo do minimo")