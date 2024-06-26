import random

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