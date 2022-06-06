print("This is a calculator application, please enter two numbers and an operator for it work !")
x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))
z = input("Please enter an operator: ")
if z == '-':
    print(x-y)
elif z == '+':
    print(x+y)
elif z == '*':
    print(x*y)
elif z == '/':
    print(x/y)
else:
    print("You have somehow messed it up. Try again")