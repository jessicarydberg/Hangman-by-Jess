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
    Creates a list of words and randomly pick and return one
    of them to play with.
    """
    words = "duck water sweater coding orange facebook computer".split(" ")
    number = random.randint(0, len(words)-1)
    word = list(words[number])

    print("Welcome to the games of HangMan!\n")
    print("Can you guess wich word is hidden?")
    print("You can guess for letters or words but be carefull...")
    print("Every incorrect guess takes you close to hanging the man...")
    print(HANGMAN[0])
    hidden_letters = []
    blank = "_"
    while len(hidden_letters) != len(word):
        hidden_letters.append(blank)
    print((''.join(hidden_letters)))
    return word, hidden_letters


def get_guess(word, hidden_letters, tries):
    """
    Lets the user make a guess and validate it.
    """
    print(word)
    print(hidden_letters)
    print((''.join(hidden_letters)))
    while True:
        guess = input("Please make a guess: ")
        if validate_guess(guess, word):
            break
    guess = list(guess)
    if guess == word:
        end_game(WIN)
    elif guess[0] in word:
        add_letter(guess, word, hidden_letters, tries)
    else:
        collect_tries(tries, word, hidden_letters)


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


def add_letter(guess, word, hidden_word, tries):
    """
    Collects correct guesses of on letter and ads it to the hidden word.
    """
    print("Hey good guess!")
    if hidden_word == word:
        end_game(WIN)
    else:
        for i in range(len(word)):
            if word[i] == guess[0]:
                hidden_word[i] = guess[0]
    if "_" in hidden_word:
        get_guess(word, hidden_word, tries)
    else:
        end_game(WIN)


def collect_tries(tries, word, hidden_letters):
    """
    Calculate how many tries wich decides wich "image"
    of the hangman should be displayed.
    """
    print("Oops bad guess, lets hang the man!")
    tries += 1
    if tries == 7:
        print(HANGMAN[tries])
        end_game(LOOSE)
    else:
        print(HANGMAN[tries])
        get_guess(word, hidden_letters, tries)


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
        main()
    else:
        print("Thank you for playing!")


def main():
    """
    main function.
    """
    tries = 0
    word, hidden_word = get_word()
    get_guess(word, hidden_word, tries)


def test():
    """
    For testing code.
    """
    testing = "alpha"
    print(testing)
    testing = list(testing)
    print(testing)
    testing = (''.join(testing))
    print(testing)


main()
# test()
