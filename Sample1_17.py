#Python Program to Count the Number of Vowels in a String
str1 = str(input("Enter the String"))
vov = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in str1:
    if i in vov:
        count = count+1
print("vowels : ",count)
