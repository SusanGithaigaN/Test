# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comnined_string = name1 + name2
# print(comnined_string)
lowercase_string = comnined_string.lower()

t= lowercase_string.count("t")
r= lowercase_string.count("r")
u= lowercase_string.count("u")
e= lowercase_string.count("e")

true = t + r + u+ e

l= lowercase_string.count("l")
o= lowercase_string.count("o")
v= lowercase_string.count("v")
e= lowercase_string.count("e")

love= l + o + v +e

love_score = int(str(true) + str(love))

# print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
     print(f"Your score is {love_score}.")   
