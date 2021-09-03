import os

# HANGMAN
hangMan=["",
        "_____     ",
        "|    |    ",
        "|    O    ",
        "|   /|\   ",
        "|   / \   ",
        "|         "]

currentHangman = [hangMan[0], hangMan[1], hangMan[2],hangMan[3][0], 
        hangMan[4][0], hangMan[5][0], hangMan[6]]
word = input("Whats the word? ")

def hangManUpdate(guessCount):
    global currentHangman
    if guessCount == 1:
        currentHangman[3] = hangMan[3]
    elif guessCount == 2:
        currentHangman[4] = "|    |    "
    elif guessCount == 3:
        currentHangman[4] = "|   /|    "
    elif guessCount == 4:
        currentHangman[4] = "|   /|\   "
    elif guessCount == 5:
        currentHangman[5] = "|   /     "
    elif guessCount == 6:
        currentHangman[5] = "|   / \   "

def collectIndexes(currentGuess):
    global word
    indexes = []
    for i,char in enumerate(word):
        if char == currentGuess:
            indexes.append(i)
    return indexes

def convert(string):
    list1=[]
    list1 = list(string)
    return list1

def hangmanMain():
    current = "_" * len(word)
    win = False
    total = 6
    guessCount = 0
    os.system('cls||clear')

    for i in currentHangman:
        print (i)
    print(current)

    while win == False and guessCount != total:
        currentGuess = str(input("Guess a Letter: "))
        if currentGuess in word:
            indexes = collectIndexes(currentGuess)
            currentList = convert(current)
            for i in indexes:
                currentList[i] = currentGuess
            current = "".join(currentList)
            for i in currentHangman:
                print(i)
            print(current)
        else:
            guessCount +=1
            hangManUpdate(guessCount)
            for i in currentHangman:
                print(i)
            print(current)
        if "_" not in current:
            win = True

    if guessCount == total:
        print("you lose")
    else:
        print("you win!")
hangmanMain()