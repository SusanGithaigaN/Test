# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

# print(type(height))
# print(type(weight))

new_height = float(height)
actual_height = new_height**2
new_weight = int(weight)

# print(actual_height)

bmi = new_weight/actual_height
new_bmi = int(bmi)
print(new_bmi)


