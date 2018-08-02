#Python program to print the lowest index in the string where substring sub is found within the string
str1 = str(input("Enter the string"))
str2 = str(input("Enter the sub string"))
ind = str1.find(str2)
print("Lowest index is ",ind)