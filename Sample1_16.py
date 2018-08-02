#Python Program to Replace all Occurrences of ‘a’ with $ in a String
str1 = str(input("Enter the String"))
str2 = ''
for ch in str1:
    if ch == 'a':
        str2 = str2+'$'
    else:
        str2 = str2 +ch
print(str2)