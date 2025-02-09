from art import art
from game_data import data
from random import randint
import os

print(art[0])
score =0
endgame = 0
while(endgame == 0):
    chA = data[randint(0,len(data)-1)]
    print(f"Compare A: {chA['name']}")
    print(art[1])
    chB = data[randint(0,len(data)-1)]
    print(f"Compare B: {chB['name']}")
    ch = input("Who has more average monthly searches? Type 'A' or 'B': ")
    ch = ch.lower()
    os.system('cls')
    if(chA['follower_count']>chB['follower_count']):
        if(ch=='a'):
            score += 1
        else:
            endgame = 1
            break
    elif(chA['follower_count']<chB['follower_count']):
        if(ch=='b'):
            score += 1
        else:
            endgame = 1
            break
    else:
        score += 1
    print(art[0])
    print(f"You are right! Current score: {score}")
print(art[0])
print(f"Sorry, that's wrong. Final score: {score}")



