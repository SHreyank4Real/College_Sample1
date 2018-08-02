#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
str1 = str(input("Enter the string"))
L,U = 0,0
for i in str1:
    if i.isupper():
        U = U+1
    elif i.islower():
        L = L+1
    else:
        pass
print("No. of Upper case is ",U)
print("No. of Lower case is ",L)