import random


HANGMAN = ["""
    +-----+
          |
          |
          |
          |
          |
        =====""", """
    +-----+
    O     |
          |
          |
          |
          |
        =====""", """
    +----+
    O    |
    |    |
         |
         |
         |
       =====""", """
    +----+
    O    |
   /|    |
         |
         |
         |
       =====""", """
    +----+
    O    |
   /|\   |
         |
         |
         |
       =====""", """
    +----+
    O    |
   /|\   |
    |    |
         |
         |
         |
       =====""", """
    +----+
    O    |
   /|\   |
    |    |
   /     |
         |
         |
       =====""", """
    +----+
    O    |
   /|\   |
    |    |
   / \   |
         |
         |
       =====""", ]


def get_word():
    """
    Welcomes the user and provide information about the game.
    Lets the user choose between three themes. Run a while loop to
    collect an input that matches the themes provided. Repeatedly requests
    data, until it is valid.

    Pick a random word to play with from the chosen theme. Create a
    "hidden word" with as many blanks as letters in the word to play with.
    """
    print("\n")
    print("Welcome to the Hangman game!\n")
    print("You can choose between three themes: Animals, Sports or Furniture")
    themes = ["animals", "sports", "furniture"]
    while True:
        theme = input("Please enter the theme you would like to play: \n")
        try:
            if theme.lower() in themes:
                break
            else:
                raise ValueError(
                    f'{theme} is not available'
                )
        except ValueError as err:
            print(f"Invalid input: {err}. Please try again!")
            continue

    theme = theme.lower()
    if theme == "animals":
        words = "duck dolphin horse lion bird mouse camel".split(" ")
    elif theme == "sports":
        words = "football climbing skiing iceskating running".split(" ")
    elif theme == "furniture":
        words = "table chair sofa bathtub wardrobe bed cabinet".split(" ")
    number = random.randint(0, len(words)-1)
    word = list(words[number].upper())

    print("\n")
    print("Can you find out which word that is hidden here?")
    print("You can guess for letters or words, but be careful...")
    print("...every incorrect guess takes you closer to hanging the man.")
    hidden_word = []
    blank = "_"
    while len(hidden_word) != len(word):
        hidden_word.append(blank)
    return word, hidden_word


def get_guess(word, hidden_word, tries):
    """
    Lets the user make a guess. Run a while loop to validate the input
    with help from validate_guess function. Repeatedly request data,
    until it is valid.
    Then checks if the guess is correct or not.
    """
    print("\n")
    if len(tries) > 0:
        print("Failed guesses: " + (' '.join(tries)).upper() + "\n")
    while True:
        guess = input("Please make a guess: \n").upper()
        print("\n")
        list_guess = list(guess)
        if validate_guess(list_guess, guess, word, hidden_word, tries):
            break
    if list_guess == word:
        print("\n")
        print(f'Good guess! {guess.upper()} is the word')
        end_game("win")
    elif len(list_guess) > 1 and list_guess != word:
        collect_tries(tries, word, hidden_word, guess)
    elif guess in word:
        add_letter(guess, word, hidden_word, tries)
    else:
        collect_tries(tries, word, hidden_word, guess)


def validate_guess(list_guess, guess, word, hidden_word, tries):
    """
    Validates the data provided in the input for guessing.
    Prints error messages if the data contains other symbols then letters.
    Prints error messages if the amount of letters are other then one or
    the same as in the word the user is supposed to guess.
    """
    try:
        if guess.isalpha():
            if len(list_guess) != len(word):
                if len(list_guess) != 1:
                    raise ValueError(
                        f'Your guess needs to contain 1 letter or\
                            {len(word)} letters'
                    )
            if len(list_guess) == 1:
                if guess in hidden_word or guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
            if len(list_guess) == len(word):
                if guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
        else:
            raise ValueError(
                "Your guess needs to contain letters only"
            )
    except ValueError as err:
        print(f"Invalid input: {err}. Please try again!")
        print("\n")
        return False

    return True


def add_letter(guess, word, hidden_word, tries):
    """
    Collects all correct guesses at the right place in the hidden word.
    Checks if there are any blanks left in the hidden word: If there are
    the game will continue, if not the game is won.
    """
    for i in range(len(word)):
        if word[i] == guess:
            hidden_word[i] = guess
    if "_" in hidden_word:
        get_guess(word, hidden_word, tries)
    else:
        print("\n")
        print("The hidden word is: " + (' '.join(word)) + "\n")
        end_game("win")


def collect_tries(tries, word, hidden_word, guess):
    """
    Collects all incorrect guesses in a list. Checks if the list contains
    7 objects wich is the total amount of tries the user has.
    If the list length is 7 the game is lost, otherwise the game continues.
    """
    print("To bad! " + f'{guess} is not in the word')
    tries.append(guess)
    print(tries)
    if len(tries) == 7:
        print("\n")
        print("The hidden word is: " + (' '.join(word)) + "\n")
        end_game("loose")
    else:
        get_guess(word, hidden_word, tries)


def end_game(result):
    """
    Prints message to inform if the game was won or lost.
    Asks the user if they want to play again or end the game.
    Run a while loop to collect a valid input from the user. The answer
    to the question needs to start with the letter y or n as in Yes or No.
    """
    if result == "win":
        print("Congratulations, you figured it out!\n")
    else:
        print("No tries left...\n")
        print(HANGMAN[7] + "\n")
        print("...you killed him!\n")
    while True:
        play = input("Want to play again? (Yes or No): \n")
        try:
            if play.lower().startswith('y') or play.lower().startswith('n'):
                break
            else:
                raise ValueError(
                    f'{play} is not a valid input'
                )
        except ValueError as err:
            print(f'{err}. Please answer Yes or No')
    if play.lower().startswith('y'):
        print("\nAwesome, lets go!")
        main()
    else:
        print("\nThank you for playing!\n")


def main():
    """
    Run all functions
    """
    tries = []
    word, hidden_word = get_word()
    print(HANGMAN[len(tries)])
    print(' '.join(hidden_word))
    get_guess(word, hidden_word, tries)


main()
