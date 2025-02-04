import os
import random
import art


ch = ' '
ch2 = ' '
print(art.logo)
ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while(ch != 'n'):
    user = []
    computer = []
    game_over = False
    os.system('cls')
    for i in range(2):
        user.append(random.randint(1,10))
    computer.append(random.randint(1,10))
    print(f"Your cards: {user}, current score: {sum(user)}")
    print(f"Computer's first card: {computer}")
    ch2 = input("Type 'y' to get another card, type 'n' to pass: ")
    while(ch2!='n' and sum(user) <=21):
        user.append(random.randint(1,10))
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer's first card: {computer}")
        if(sum(user) >21):
            print(f"Your final hand: {user}, final score: {sum(user)}")
            print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
            print("You went over. You lose 😭")
            game_over = True
            break
        ch2 = input("Type 'y' to get another card, type 'n' to pass: ")
    flag = 0
    while(sum(computer)<17 and game_over == False):
        computer.append(random.randint(1,10))
        if(sum(computer)>21):
            flag = 1
    print(f"Your final hand: {user}, final score: {sum(user)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    if(flag == 1):
        print("Opponent went over. You win 😁 ")
    elif(sum(user) < sum(computer)):
        print("You lose 😤 ")
    elif(sum(user) == sum(computer)):
        print("Its a Draw.")
    else:
        print("You Won")
    ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    