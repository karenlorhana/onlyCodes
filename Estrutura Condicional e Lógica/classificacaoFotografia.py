PSNR = float(input())
enquadramento = str(input())
exposicao = str(input())

if (80 <= PSNR <= 90):
    if (enquadramento == "bom" or enquadramento == "excelente"):
        if (exposicao == "bem exposta"):
            print("para imprimir")
        else:
            print("boa")
    else:
        print("marromeno")

elif (50 <= PSNR < 80):
    if (enquadramento == "excelente"):
        if (exposicao == "bem exposta"):
            print("boa")
    else:
        print("marromeno")

elif (PSNR < 50):
    if (enquadramento == "excelente"):
        if (exposicao == "bem exposta"):
            print("marromeno")
        else:
            print("lixo")
    else:
        print("lixo")