#Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique
import random
s = set()

while len(s)<5:
    s.add(random.randint(1,20))

print(s)