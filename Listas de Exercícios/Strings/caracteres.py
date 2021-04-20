while True:
    numero = input()
    if numero == "0":
        break
    nome = input()
    palavra = ""
    for letra in nome:
            palavra = letra + palavra
    print(palavra)