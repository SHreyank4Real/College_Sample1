#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
str1 = str(input("Enter the String 1 "))
str2 = str(input("Enter the String 2 "))
count1,count2 = 0,0
for i in str1:
    count1 = count1+1
for i in str2:
    count2 = count2+1

if count1 > count2:
    print("String 1 is large")
else:
    print("String 2 is large")
