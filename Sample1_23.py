#Python Program to check whether a full pattern (not sub string) is present in the given sentence
str1 = str(input("Enter the string"))
str2 = str(input("Enter the patern"))

str3 = str1.split(' ')
if str2 in str3:
	print("Patern Found")
else:
	print("Patern Not Found")
