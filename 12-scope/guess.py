#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import randint
# set difficulty as global constants 
EASY_LEVEL = 10 
HARD_LEVEL = 5

# turns = 0

'''Check user's answer'''
def check_answer(guess,answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}.")

# make function to set difficulty
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    # set no of attempts
    return EASY_LEVEL
  elif difficulty == "hard":
    return HARD_LEVEL
  else: 
    print("Invalid input, please try again")

def game():
  '''Check answer against guess and return the number of turns remaining'''
  # choose a random no btwn 1 & 100
  print("Welcome to he guessing game")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)
  # show answer
  print(f"The correct answer is {answer}")
  
  turns = set_difficulty()
  # print(f"You have {turns} attempts remaining to guess the number")
  
  # repeat guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    # let user guess a num
    guess = int(input("Guess a number: "))
    # check user's guess against actual answer
    turns = check_answer(guess,answer, turns)
    #  track num of turns and reduce by 1 if user gets it wrong

    # end game when turns = 0
    if turns == 0:
      print("You've run out of guesses, you lose")
      # exit and end the function
      return
    elif guess != answer:
      print("Guess again")
  
game()  