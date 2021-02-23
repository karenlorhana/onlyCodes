idadeJogador = int(input())
tipoJogo = str(input())

if (idadeJogador < 0 or idadeJogador > 130):
    print("Idade invalida.")

elif(tipoJogo == "azar" and idadeJogador >= 21):
    print("Pode entrar!")
elif(tipoJogo == "azar" and idadeJogador <21):
    print("Volte daqui há alguns anos.")

elif(tipoJogo == "mmorpg" and idadeJogador >= 14):
    print("Pode entrar!")
elif(tipoJogo == "mmorpg" and idadeJogador < 14):
    print("Volte daqui há alguns anos.")

elif(tipoJogo == "moba" and idadeJogador >= 10):
    print("Pode entrar!")
elif(tipoJogo == "moba" and idadeJogador <10):
    print("Volte daqui há alguns anos.")

elif (tipoJogo == "casual"):
    print("Pode entrar!")
else:
    print("Jogo invalido.")