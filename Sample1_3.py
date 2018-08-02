#Python Program to Print all Numbers in a Range Divisible by a Given Number. [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
r= int(input("Enter the range"))
num = int(input("Enter the number"))
divList = []

for i in range(1,r+1):
    if i%num == 0:
        divList.append(i)

print(divList)
