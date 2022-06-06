x = int(input("Please enter the line length"))
y = input("Do you want a horizontal or vertical line?")
if y == "vertical" or y == "Vertical":
    for x in range(0,x):
        print('*')
elif y == "horizontal" or y == "Horizontal":
    for x in range(0,x):
        print(x, end=' ')
    print('*')
else:
    print("You did something wrong, Try again")