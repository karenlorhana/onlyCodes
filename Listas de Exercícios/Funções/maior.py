def maior(num):
    maior=0
    for i in range(len(num)):
        if(maior < int(num[i])):
            maior = int(num[i])
    return maior

print(maior(input().split()),"eh o maior")