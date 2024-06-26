import random
import sys
from termcolor import colored

def print_menu():
    print("Let's Play Wordle")
    print("Type 6 letter word and enter")

def random_word():
    with open ("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

print_menu()
word = random_word()
print(word)

for tries in range (1, 8):
    guess = input().lower()

    for i in range(min(len(guess), 6) and range(max(len(guess)), 6)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess [i] in word:
            print(colored(guess[i], 'blue'), end="")
        else:
            print(guess[i], end ="")
        
        if guess == word:
            print(colored(f"Congratulations! You got the world in {i}", 'pink'))