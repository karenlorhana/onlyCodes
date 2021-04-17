aux = 0
seq = 1
seqMax = 0

qtd = int(input("qtd: "))
n = str(input("valroes: ")).split(" ")

for num in range(qtd-1):
    if n[num] == n[num+1]:
            
            seq += 1
    else: 
        seq = 1
    if seq > seqMax:
        seqMax = seq
    
print(seqMax)


#1 1 1 20 20 20 20 3 3 3 3 3 3 3