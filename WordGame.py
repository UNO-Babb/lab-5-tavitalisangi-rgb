#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter = word[spot]
    if  letter == correctLetter:
        return True
    else:
        return False 
  

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback+myLetter.upper()
        elif inWord(myLetter, word) == True:
            feedback = feedback+myLetter.lower()
        else:
            feedback = feedback + "*"
    return feedback


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    #print(todayWord)

    guessNum = 1
    while guessNum <= 6:
        validWord = False
        while validWord == False:
            guess = input("Enter a guess: ")
            guess = guess.lower()
            if guess not in wordList:
                print("Word not in list.")
                validWord = False
            else:
                validWord = True
        feedback = rateGuess(guess, todayWord)
        print(feedback)
        if feedback == todayWord.upper():
            print("Youu got it in", guessNum, "tries!")
            break

        guessNum = guessNum + 1
    print("The word was", todayWord)
    print("Bye!")
    #User should get 6 guesses to guess

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
