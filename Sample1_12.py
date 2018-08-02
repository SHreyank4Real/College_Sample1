#Python Program to Check if a Number is a Palindrome
num = input("Enter the number")
num = str(num)
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not PalinSample1_drome")