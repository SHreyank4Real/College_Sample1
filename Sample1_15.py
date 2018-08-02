#Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.
str1 = str(input("Enter the String"))
if str1.isalnum():
    print("True")
else:
    print("False")