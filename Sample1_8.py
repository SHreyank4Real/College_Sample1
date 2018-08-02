#Python Program to Read a number n and Compute n+nn+nnn.
n = int(input("Enter the value of n"))
nn = str(n)+str(n)
nnn = str(n)+str(n)+str(n)
n = n +int(nn)+int(nnn)
print("value of n is ",n)