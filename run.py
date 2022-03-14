import random

WIN = "win"
LOOSE = "loose"

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
        result = WIN
    elif guess[0] in word:
        result = add_letter(guess, word, tries)
    else:
        result = collect_tries(tries, word)
    print(result)
    return result


def validate_guess(guess, word):
    """
    Validates the data provided.
    """
    if guess.isalpha():
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


def add_letter(guess, word, tries):
    """
    Collects correct guesses of on letter and ads it to the hidden word.
    """
    print("Hey good guess!")
    hidden_word = []
    if hidden_word == word:
        return WIN
    else:
        get_guess(word, tries)


def collect_tries(tries, word):
    """
    Calculate how many tries wich decides wich "image"
    of the hangman should be displayed.
    """
    print("Oops bad guess, lets hang the man!")
    tries += 1
    if tries == 7:
        print(HANGMAN[tries])
        return LOOSE
    else:
        print(HANGMAN[tries])
        print("_" * len(word))
        get_guess(word, tries)


def end_game(result):
    """
    Prints a message depending on if game is lost or won.
    Gives user oportunity to play again.
    """
    print(result)
    if result == "win":
        print("Hey you won the game!")
    elif result == "loose":
        print("...Oh no!\n")
        print("No tries left...\n")
        print("...you killed him!")
    while True:
        play_again = input("Want to play again? (Y/N)")
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Invalid input, please insert Y for yes or N for No!")
    if play_again == "Y":
        return False
    else:
        return True


def main():
    """
    main function.
    """
    while True:
        tries = 0
        hidden_word = get_word()
        result = get_guess(hidden_word, tries)
        print(result)
        if end_game(result):
            break
    print("Thanks for playing!")


main()