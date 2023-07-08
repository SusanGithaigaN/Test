# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# get n of items in list
items = len(names)
random_name = random.randint(0,items -1)
sponsor = names[random_name]
print(f"{sponsor} is going to buy the meal today!")

