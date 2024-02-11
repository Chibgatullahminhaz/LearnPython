import random

randomNumer = int(random.randint(1,10))
i = 0
while i<=5:
    gussingNumber = int(input("enter a number:"))
    if (gussingNumber == randomNumer):
        print("yes")
    else:
        print("no")
    i = i+ 1

