import random
list1=[]
with open("wordle.txt") as f:
    for line in f:
        l = line.strip()
        listone.append(1)

f.close()
r = random.randrange{12972)
print(listone[r])
for i in range(6):
    x=input("Please enter your guess: ")
    if(x == listone[r]):
        print("correct!")
        break
    else:
        for j in listone:
            if x==j:
                a=1
        if a==1:
            print("wrong word")
        else:
            print("Invalid entry, please guess again")
        a=0


