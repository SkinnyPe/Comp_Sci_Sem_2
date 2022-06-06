import random
x = int(input("How many numbers would you like to print?"))
list1=[]
print("Your random numbers are ",end="")
for i in range(0,x):
    list1.append(random.randrange(1,11))
    print(str(list1[])+", ", end=" ")