#Python Program to Reverse a Given Number.
num=int(input("Enter number: "))
rev=0
dig=0

while num>0:
    dig=num%10
    num=num//10 #returning only int value
    rev =rev*10+dig
print("Reverse :",rev)

#method2 works for 100

num = int(input("Enter the number :"))
rev = ""
dig = 0
while num>0:
    dig = num%10
    num=num//10
    rev=rev+str(dig)
print("reverse is :",rev)

