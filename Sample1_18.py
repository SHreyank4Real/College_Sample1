#Python Program to Take in a String and Replace Every Blank Space with Hyphen
str1 = str(input("Enter the String"))
str2 = ''
for ch in str1:
    if ch == ' ':
        str2 = str2+'~'
    else:
        str2 = str2 +ch
print(str2)