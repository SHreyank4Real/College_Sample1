#Python Program to Calculate the Average of Numbers in a Given List

list1 = [1,2,3,4,5,6,7,10]
length = len(list1)
sum = 0
print(list1)
for i in list1:
    sum =sum+i

print("Avg of list is ",sum/length)