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

    print("\n")
    print("Welcome to the games of HangMan!\n")
    print("Can you guess wich word is hidden?")
    print("You can guess for letters or words but be carefull...")
    print("Every incorrect guess takes you closer to hanging the man...")
    hidden_letters = []
    blank = "_"
    while len(hidden_letters) != len(word):
        hidden_letters.append(blank)
    return word, hidden_letters


def get_guess(word, hidden_letters, tries):
    """
    Lets the user make a guess and validate it.
    """
    print(HANGMAN[len(tries)])
    print((' '.join(hidden_letters)).upper() + "\n")
    if len(tries) > 0:
        print("Guessed: " + (', '.join(tries)).upper() + "\n")
    while True:
        guess = input("Please make a guess: ")
        print("\n")
        if validate_guess(guess, word, hidden_letters, tries):
            break
    guess = list(guess)
    if guess == word:
        end_game(WIN)
    elif len(guess) > 1 and guess != word:
        collect_tries(tries, word, hidden_letters, guess)
    elif guess[0] in word:
        add_letter(guess, word, hidden_letters, tries)
    else:
        collect_tries(tries, word, hidden_letters, guess)


def validate_guess(guess, word, hidden_letters, tries):
    """
    Validates the data provided.
    """
    if guess.isalpha():
        if len(list(guess)) == len(word):
            return True
        elif len(list(guess)) == 1:
            if guess[0] in hidden_letters or guess[0] in tries:
                print(f'You already guessed for {guess}')
                print("Please try another guess!")
                return False
            else:
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
    print("Good guess!\n")
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


def collect_tries(tries, word, hidden_letters, guess):
    """
    Calculate how many tries wich decides wich "image"
    of the hangman should be displayed.
    """
    print("Oops bad guess...\n")
    tries.append(''.join(guess))
    if len(tries) == 7:
        end_game(LOOSE)
    else:
        get_guess(word, hidden_letters, tries)


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
        print("...you killed him!\n")
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
        print("Thank you for playing!")


def main():
    """
    main function.
    """
    tries = []
    word, hidden_word = get_word()
    get_guess(word, hidden_word, tries)


main()
