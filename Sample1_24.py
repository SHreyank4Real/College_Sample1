#Cumulative sum of a list [1, 2, 4, …] is defined as  [1, 3, 7, . . .] Write a function cumulative_sum() to compute cumulative sum of a list
def cumulative(l):
    l2 = []
    size= len(l)

    for i in range(0,size):
        l2.append(sum(l[0:i+1]))
    print(l2)

l = [1,2,3,4,5]
cumulative(l)