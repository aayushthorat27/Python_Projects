import art
import random
def guess(guess,actual):
    if(guess>actual):
        print("Too high")
    elif(guess < actual):
        print("Too low")
    else:
        print(f"You got it! The answer was {actual}")
        return True
    return False

print(art.logo)
actual = random.randint(1,100)
difficulty = input("""Welcome to the Numbver Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """)
attempts =0
flag = False
if(difficulty == "easy"):
    attempts = 10
else:
    attempts = 5
for i in range(attempts):
    print(f"You have {attempts-i} attempts remaining to guess the number.")
    trial = int(input("Make a guess: "))
    flag = guess(trial,actual)
    if(flag == True):
        break
if(flag == False):
    print("You Lost! You couldnt guess withing the no.of attempts")
