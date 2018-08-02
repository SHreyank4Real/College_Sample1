#Python Program to Find the Smallest Divisor of an Integer.
num = int(input("Enter number : "))
small = 1
for i in range(num,1,-1):
    if num%i==0:
        small = i
print("smallest Divisor is ",small)

