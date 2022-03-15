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
    print("\n")
    print("Welcome to the games of HangMan!\n")
    print("You can choose between three themes: Animals, Sports or Furniture")
    themes = ["animals", "sports", "furniture"]
    while True:
        theme = input("Please enter the theme you would like to play here: ")
        if theme.lower() in themes:
            break
        else:
            print(f'{theme} is not available, please try again!')
            continue

    theme = theme.lower()
    if theme == "animals":
        words = "duck dolphine horse lion bird mouse camel".split(" ")
    elif theme == "sports":
        words = "football climbing skiing iceskating running".split(" ")
    elif theme == "furniture":
        words = "table chair sofa bathtub wardrobe bed cabinet".split(" ")
    number = random.randint(0, len(words)-1)
    word = list(words[number])

    print("\n")
    print("Can you guess wich word is hidden?")
    print("You can guess for letters or words but be carefull...")
    print("Every incorrect guess takes you closer to hanging the man...")
    hidden_word = []
    blank = "_"
    while len(hidden_word) != len(word):
        hidden_word.append(blank)
    return word, hidden_word


def get_guess(word, hidden_word, tries):
    """
    Lets the user make a guess and validate it.
    """
    print(HANGMAN[len(tries)])
    print((' '.join(hidden_word)).upper() + "\n")
    if len(tries) > 0:
        print("Guessed: " + (', '.join(tries)).upper() + "\n")
    while True:
        guess = input("Please make a guess: ")
        print("\n")
        if validate_guess(guess, word, hidden_word, tries):
            break
    guess = list(guess)
    if guess == word:
        end_game(WIN)
    elif len(guess) > 1 and guess != word:
        collect_tries(tries, word, hidden_word, guess)
    elif guess[0] in word:
        add_letter(guess, word, hidden_word, tries)
    else:
        collect_tries(tries, word, hidden_word, guess)


def validate_guess(guess, word, hidden_word, tries):
    """
    Validates the data provided.
    """
    try:
        if guess.isalpha():
            if len(list(guess)) != len(word):
                if len(list(guess)) != 1:
                    raise ValueError(
                        f'Your guess needs to contain 1 letter or\
                            {len(word)} letters'
                    )
            if len(guess) == 1:
                if guess[0] in hidden_word or guess[0] in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
            if len(guess) == len(word):
                if (''.join(guess)) in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
        else:
            raise ValueError(
                "Your guess needs to contain letters only"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again!")
        return False

    return True


def add_letter(guess, word, hidden_word, tries):
    """
    Collects correct guesses of on letter and ads it to the hidden word.
    """
    print("Good guess!\n")
    if hidden_word == word:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game(WIN)
    else:
        for i in range(len(word)):
            if word[i] == guess[0]:
                hidden_word[i] = guess[0]
    if "_" in hidden_word:
        get_guess(word, hidden_word, tries)
    else:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game(WIN)


def collect_tries(tries, word, hidden_word, guess):
    """
    Calculate how many tries wich decides wich "image"
    of the hangman should be displayed.
    """
    print("Oops bad guess...\n")
    tries.append(''.join(guess))
    if len(tries) == 7:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game(LOOSE)
    else:
        get_guess(word, hidden_word, tries)


def end_game(result):
    """
    Prints a message depending on if game is lost or won.
    Gives user oportunity to play again.
    """
    if result == "win":
        print("Hey you won the game!\n")
    elif result == "loose":
        print("...Oh no!\n")
        print("No tries left...\n")
        print("...you killed him!")
        print(HANGMAN[7] + "\n")
    while True:
        play_again = input("Want to play again? (Y/N)")
        play_again = play_again.upper()
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Invalid input, please insert Y for Yes or N for No!")
    if play_again == "Y":
        main()
    else:
        print("\nThank you for playing!\n")


def main():
    """
    main function.
    """
    tries = []
    word, hidden_word = get_word()
    get_guess(word, hidden_word, tries)


main()
