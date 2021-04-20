x = int(input())

while x != -1:
    divisores = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisores += 1
    if divisores == 2:
        print("1")
    else:
        print("0")
    x = int(input())

