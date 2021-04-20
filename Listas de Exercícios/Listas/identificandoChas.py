t = int(input())
x = input()
x = x.split(' ')
r = 0

for i in range(5):
    if int(x[i]) == t:
        r += 1

print(r)