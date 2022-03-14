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
    print("Every incorrect guess takes you close to hanging the man...")
    print(HANGMAN[0])
    print("_" * len(word))
    return word


def get_guess(word, tries):
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
        return win_game()
    elif guess[0] in word:
        add_letter(guess, word)
    else:
        collect_tries(tries, word)
 

def validate_guess(guess, word):
    """
    Validates the data provided.
    """
    if guess.isalpha():
        print(len(list(guess)), len(word))
        if len(list(guess)) == len(word):
            return True
        elif len(list(guess)) == 1:
            return True
        else:
            print(f"Invalid data: {guess}.")
            print(f'Your guess needs to be one letter or {len(word)} letters.')
            print("Please try again.\n")
            return False
    else:
        print(f"Invalid data: {guess}.")
        print("Your guess needs to be only letters, please try again.\n")
        return False


def add_letter(guess, word):
    """
    Collects correct guesses of on letter and ads it to the hidden word.
    """
    print("Hey good guess!")


def collect_tries(tries, word):
    """
    Calculate how many tries wich decides wich "image" 
    of the hangman should be displayed.
    """
    print("Oops bad guess, lets hang the man!")
    tries += 1
    print(HANGMAN[tries])
    print("_" * len(word))
    get_guess(word, tries)


def win_game():
    """
    Congratulates when game is completed and asks if 
    the user wants to play again.
    """
    print("Hey you won the game!")
    while True:
        play_again = input("Want to play again? (Y/N)")
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Invalid input, please insert Y for yes or N for No!")
    if play_again == "Y":
        return True
    else:
        return False


def main():
    """
    main function.
    """
    while True:
        tries = 0
        hidden_word = get_word()
        if not get_guess(hidden_word, tries):
            break
    print("Thanks for playing!")


main()