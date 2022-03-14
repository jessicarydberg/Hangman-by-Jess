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

    print("Welcome to the games of HangMan!\n")
    print("Can you guess wich word is hidden?")
    print("You can guess for letters or words but be carefull...")
    print("Everytime you make an incorrect guess you will get closer to hanging the man...")
    print(HANGMAN[0])
    print("_" * len(word))
    return word


def get_guess(word):
    """
    Lets the user make a guess and validate it.
    """
    print(word)
    while True:
        guess = input("Please make a guess: ")
        if validate_guess(guess, word):
            break
    guess = list(guess)
    if guess == word:
        win_game()
    elif guess[0] in word:
        add_letter(guess, word)
    else:
        collect_tries()
      

def validate_guess(guess, word):
    """
    Validates the data provided.
    """
    if guess.isalpha():
        guess = list(guess)
        print(len(guess), len(word))
        if len(guess) == len(word):
            return True
        elif len(guess) == 1:
            return True
        else:
            print(f"Invalid data: {guess}, please try again.\n")
            return False 
    else:
        print(f"Invalid data: {guess}, please try again.\n")
        return False


def add_letter(guess, word):
    """
    Collects correct guesses of on letter and ads it to the hidden word.
    """
    print("Hey good guess!")


def collect_tries():
    """
    Calculate how many tries wich decides wich "image" 
    of the hangman should be displayed.
    """
    print("Lets hang the man!")


def win_game():
    """
    Congratulates when game is completed and asks if 
    the user wants to play again.
    """
    print("Hey you won the game!")


def main():
    hidden_word = get_word()
    get_guess(hidden_word)


main()