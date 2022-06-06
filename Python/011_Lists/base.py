print("This is a random joke generator!")
one = "Why was six afraid of seven?.... Because seven eight nine."
two = "What do you call a hippie’s wife?.... Mississippi."
three = "What do you call a bear with no teeth?.... A gummy bear"
four = "How much did Santa pay for his sleigh?.... Nothing, it was on the house"
five = "Why don’t cats play poker in the jungle?.... Too many cheetahs."
list1 = [one, two, three, four, five]
import random
x = (random.randrange(0,4))
print(list1[x])