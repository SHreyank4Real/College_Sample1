#Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
import random

list1 = []
start = 1
step = 10

while len(list1) < 10:
    list1.append(random.randint(start,step))
    start = step+1
    step += 10

print(list1)