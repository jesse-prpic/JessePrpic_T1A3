# imports
# to allow me to use a random input of my choosing
import random
import sys
# Allowing the system to have color added to certain objects whether they are incoorect or not
from termcolor import colored

# Defining the print menu and the introduction to the game
def game_intro():
        print("Let's play")
        print("Type a six-letter word and enter!\n")

# Defining the input and connecting the import of the main.py to words.txt
def random_word():
        with open ("words.txt") as f:
            words = f.read().splitlines()
            return random.choice(words)

# creating a loop to allow the player to choose whether to play again or to exit
game_intro()
play_again = " "
while play_again != "e":
    word = random_word()
    for tries in range (1, 8):
        guess = input().upper()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

# Syntax being able to restict the player to only play a 6 letter word, if any less or any more there will be an error
        for word_length in range(min(len(guess), 6)) and range(max(len(guess), 6)):
            if guess[word_length] == word[word_length]:
                print(colored(guess[word_length], "black", "on_light_green"), end=" ")
            elif guess [word_length] in word:
                print(colored(guess[word_length], "black", "on_yellow"), end=" ")
            else:
                print(guess[word_length], end =" ")
        print()

# Defining what the outcome of the game will be, whether the player wins or not
        if guess == word:
            print(colored(f"Congratulations! You got the wordle in {tries}" , "white", "on_magenta", attrs=["bold"]))
            break
        elif tries == 6:
             print(colored(f"Better luck next time - the word was... {word} ", "white", "on_red", attrs=["bold"]))
    play_again = input("Want to play again? Press enter and guess another word. \n Type 'e' to exit")

     