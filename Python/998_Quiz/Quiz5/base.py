x = (input("What is your favorite number? "))
first = print("My favorite number is " + x)
y = (input("What is your age? "))
second = print("My age is " + y)
first = []
count1 = 0
for i in range(0,len(first)): I MAKE A COUNTER THAT COUNTS TWO SPACES OF THE SENTENCE AND IF IT EQUALS x, or the number, 
    if(first[i+1:i+2] == x):  I HAD TO HAVE MADE A COUNTER THAT ACCOUNTS FOR ANY NUMBER AND SO THAT THE COUNTER CAN COUNT
        print(x)              I NEED TO MAKE A LOOP THAT DOES THAT EXACT PURPOSE, AFTER THAT I DUPLICATE THE SAME EXACT LOOP FOR
        count1 = count1 + 1   THE SENTENCE FOR THE AGE AND THEN MULTIPLY
second = []
count2 = 0
for j in range(0,len(second)):
    if(second[j+1,j+2] == y):
        print(y)
        count2 = count2 + 1
final = (int(print(x*y))) I HAVE TO CAST THIS INTO TWO INTEGERS SO THAT I CAN MULTIPLY THEM TOGETHER
