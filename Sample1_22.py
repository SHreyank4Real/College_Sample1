#Python Program to Calculate the Number of Digits and Letters in a String
str1 = str(input("Enter the String"))
D,L=0,0
for i in str1:
    if i.isdigit():
        D=D+1
    elif i.isspace():
        pass #ignoreing the space
    else:
        L=L+1
print("Number of Digit is    ",D)
print("Number of Letters are ",L)