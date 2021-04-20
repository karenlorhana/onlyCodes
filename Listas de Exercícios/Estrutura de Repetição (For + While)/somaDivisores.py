numUm = int(input())
numDois = int(input())
numTres = int(input())
numQuatro = int(input())
numCinco = int(input())
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0

for i in range(1,numUm+1):
    if(numUm%i == 0):
        t1 += i
for i in range(1,numDois+1):
    if(numDois%i == 0):
        t2 += i
for i in range(1,numTres+1):
    if(numTres%i == 0):
        t3 += i
for i in range(1,numQuatro+1):
    if(numQuatro%i == 0):
        t4 += i
for i in range(1,numCinco+1):
    if(numCinco%i == 0):
        t5 += i
        
if(t1>=t2 and t1>=t3 and t1>=t4 and t1>=t5):
    print(numTres)
elif(t2>=t1 and t2>=t3 and t2>=t4 and t2>=t5):
    print(numDois)
elif(t3>=t2 and t3>=t1 and t3>=t4 and t3>=t5):
    print(numTres)
elif(t4>=t2 and t4>=t3 and t4>=t1 and t4>=t5):
    print(numQuatro)
else:
    print(numCinco)