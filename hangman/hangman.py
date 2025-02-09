import hangs
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')


word = "aayush"
guessed = []
left = len(word)
errors = 0
while left != 0:
    while cont != 0:
        letter = input("Guess a letter: ")
        if letter in guessed:
            print("You have already tried this letter!")
            cont = 1
        else:
            cont = 0
    for i in range(len(word)):
        print("_",end=" ")
    print(end="\n")
    if letter in word:
        print("You have guessed coorect!")
        guessed.append(letter)
        left -= word.count(letter)
    else:
        print("You guessed worng")
        print(hangs.tries[errors])
        errors += 1
    if (errors == 7):
        print("You Lost!")
        break
    elif (left == 0):
        print("You Won!")

    for i in range(len(word)):
        if word[i] in guessed:
            print(word[i],end=" ")
        else:
            print("_",end=" ")