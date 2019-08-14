from typing import List, TextIO
from random import randrange

hangman = ["  __     ",
"/ . . \\ ",
"|  >  |  ",
"| --  |  ",
"\\ __  /",
"   |   ",
"\\  | /",
"   |  ",
"   |  ",
" /   \\"]
file = open("words.txt", "r")
text = file.read()
word_list = text.split()

print("Hangman");
#word_list = ['pizza', 'hamburger', 'chicken', "meatloaf", "spaghetti","fists", "fives", "fixes", "fixed"]
number_of_guesses = 10
guess_count: int = 0
guessed_letters = []

word = word_list[randrange(len(word_list))]


guess_word = []

for i in range(len(word)):
    guess_word.append('_')

def print_guess_word():
    print_word = []
    for j in range(len(guess_word)):
        print_word.append(guess_word[j])
        print_word.append(' ')
    print("".join(print_word))

print_guess_word()

while True:
    x = input("Enter your guess")
    if x == "":
        continue
    x = x.lower()
    guess_letter = x[0]
    print("You guessed: " + guess_letter)

    #add guessed_letters
    guessed_letters.append(guess_letter)
    print(guessed_letters)
    # check if letter is in word
    correct_guess = False
    for i in range(len(word)):
        if word[i] == guess_letter:
            guess_word[i] = guess_letter
            correct_guess = True
    # YES PATH
    #update guess_word
    # any guessed letters
    # no letters left (you win)
    if "".join(guess_word).find("_") == -1:
        print("You Win! " + word)
        break


    #NO PATH
    # increment bad guess count
    if not correct_guess:
        guess_count += 1
        print(f'You have {number_of_guesses - guess_count} guesses remaining')
    # print hangman
    if not correct_guess:
        for i in range(guess_count):
            print(hangman[i])

    # any guesses left
    if number_of_guesses == guess_count:
        print("You Lose " + word)
        break
    # NO (you lose)

    print_guess_word()


