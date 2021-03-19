''' 
    Developed by Karen Lorhana
'''

while True:
    num = int(input())
    if num == -1:
        break
    else:
        total = 1
        for i in range(num):
            total = total *(i+1)
        print(total)