# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# size_s = 15
# size_m = 20
# size_l = 25

# pepperoni = 2
# pepperoni_ml = 3
# cheese = 1

# if size == S:
#     if size == M:
#         if size == L:
#             if size == s and add_pepperoni == Y


bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")