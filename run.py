import random

HANGMAN = ["""
    +---+
        |
        |
        |
        |
        |
      =====""", """
    +---+
    O   |
        |
        |
        |
        |
      =====""", """
    +---+
    O   |
    |   |
        |
        |
        |
      =====""", """
    +---+
    O   |
   /|   |
        |
        |
        |
      =====""", """
    +---+
    O   |
   /|\  |
        |
        |
        |
      =====""", """
    +---+
    O   |
   /|\  |
    |   |
        |
        |
        |
      =====""", """
        +---+
    O   |
   /|\  |
    |   |
   /    |
        |
        |
      =====""", """
    +---+
    O   |
   /|\  |
    |   |
   / \  |
        |
        |
      =====""", ]


def get_word():
    """
    Creates a list of words and randomly pick and return one of 
    them to play with.
    """
    words = "duck water sweater coding orange facebook computer".split(" ")
    number = random.randint(0, len(words)-1)
    word = list(words[number])
    return word


def get_guess(word):
    """
    Lets the user make a guess and check if it is valid.
    """
    while True:
        guess = input("Insert your guess of caracter of word: ")
        if validate_guess(guess, word):
            break


def validate_guess(guess, word):
    """
    Checks if the guess was correct or not.
    """
    if guess.isalpha():
        guess = list(guess)
        print(guess)
        print(word)
        print(len(guess), len(word))
        if len(guess) == 1 or len(guess) == len(word):
            return True
        else:
            print(f"Invalid data: {guess}, please try again.\n")
            return False  
    else:
        print(f"Invalid data: {guess}, please try again.\n")
        return False


def collect_tries():
    """
    Calculate how many tries wich decides wich "image" 
    of the hangman should be displayed.
    """


def win_game():
    """
    Congratulates when game is completed and asks if 
    the user wants to play again.
    """


def main():
    hidden_word = get_word()
    guess = get_guess(hidden_word)


main()