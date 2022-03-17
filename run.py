import random

HANGMAN = ["""
            +------+
                   |
                   |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
                   |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
            |      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
           /       |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
           / \     |
                   |
                   |
                 =====""", ]


def get_word():
    """
    Welcome the user and provide information about the game.
    Let the user choose between three themes. Run a while loop to
    collect an input that matches the themes provided. Repeatedly requests
    data, until it is valid.

    Pick a random word to play with from the chosen theme. Create a
    "Hidden word" with as many blanks as letters in the word to play with.
    """
    print("\n")
    print("Welcome to Hangman by Jess!\n")
    print("Lets play!\n")
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
        words = "football climbing skiing tennis running".split(" ")
    elif theme == "furniture":
        words = "table chair sofa bathtub wardrobe bed cabinet".split(" ")
    number = random.randint(0, len(words)-1)
    word = list(words[number].upper())

    print("\n")
    print("Can you find out which word is hidden here?")
    print("You can guess for letters or words, but be careful...")
    print("...every incorrect guess takes you closer to hanging the man.")
    blank = "_"
    hidden_word = []
    while len(hidden_word) != len(word):
        hidden_word.append(blank)
    return word, hidden_word


def get_guess(word, hidden_word, tries):
    """
    Let the user make a guess. Run a while loop to validate the input
    with help from validate_guess function. Repeatedly request data
    until it is valid, then check if the guess is correct or not.
    """
    while True:
        print("\n")
        guess = input("Please make a guess: \n").upper()
        print("\n")
        list_guess = list(guess)
        if validate_guess(list_guess, guess, word, hidden_word, tries):
            break
    if guess in word or list_guess == word:
        return guess, "correct"
    else:
        return guess, "fail"


def validate_guess(list_guess, guess, word, hidden_word, tries):
    """
    Validate the data provided in the input for guessing.
    Print error messages if the data contains other symbols then letters.
    Print error messages if the number of letters are other than one or
    the same as in the word the user is supposed to guess.
    """
    try:
        if guess.isalpha():
            if len(list_guess) != len(word):
                if len(list_guess) != 1:
                    raise ValueError(
                        f'Your guess needs to contain 1 or {len(word)} letters'
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
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word) + "\n")
        print(f"Invalid input: {err}. Please try again!" + "\n")
        print("Failed guesses: "+(' '.join(tries)).upper())
        return False

    return True


def add_letter(guess, word, hidden_word):
    """
    Collect all correct guesses at the right place in the hidden word.
    Check if there are any blanks left in the hidden word: If there are
    the game will continue, if not the game is won.
    """
    if list(guess) == word:
        return "win"
    else:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        if "_" in hidden_word:
            return hidden_word
        else:
            return "win"


def collect_tries(tries, guess):
    """
    Collects all incorrect guesses in a list. Check if the list contains
    7 objects which is the total amount of tries the user has.
    If the list length is 7 the game is lost, otherwise the game continues.
    """
    tries.append(guess)
    if len(tries) == 7:
        return "loose"
    else:
        return tries


def end_game(saved, killed):
    """
    Run a while loop asking the user if they want to play again. Repeatedly
    request data until it is valid.
    Ends game or returns to get_word depending on the input.
    """
    if saved == 1:
        print("You have managed to save 1 man")
    else:
        print(f'You have managed to save {saved} men')
    if killed == 1:
        print("and kill 1 man.")
        print("\n")
    else:
        print(f'and kill {killed} men.')
        print("\n")
    while True:
        play = input("Do you want to try again? (Yes or No): \n")
        try:
            if play.lower().startswith('y') or play.lower().startswith('n'):
                break
            else:
                raise ValueError(
                    f'{play} is not a valid input'
                )
        except ValueError as err:
            print(f'{err}. Please answer Yes or No!')
    if play.lower().startswith('y'):
        print("\nAwesome, lets go!")
        return False
    else:
        print("\nThank you for playing!\n")
        return True


def main():
    """
    Run all functions and print appropriate messages.

    Run all functions and print appropriate messages in a while loop that
    breaks at the end of the game if the player doesn't want to play again.
    Run another while loop inside of this. Repeatedly requests for
    guesses and breaks when the game is won or lost.
    """
    saved = 0
    killed = 0
    while True:
        tries = []
        word, hidden_word = get_word()
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word))
        while True:
            guess, result = get_guess(word, hidden_word, tries)
            if result == "fail":
                result = collect_tries(tries, guess)
                if result == "loose":
                    print(HANGMAN[7] + "\n")
                    print("To bad! " + f'{guess} is not in the word.')
                    print("\n")
                    print("The hidden word is: " + (' '.join(word)) + "\n")
                    print("No tries left...\n")
                    print("...you killed him!\n")
                    killed += 1
                    break
                elif result == tries:
                    tries = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print("To bad! " + f'{guess} is not in the word.' + "\n")
                    print("Failed guesses: "+(' '.join(tries)).upper())
            elif result == "correct":
                result = add_letter(guess, word, hidden_word)
                if result == "win":
                    print(' '.join(word) + "\n")
                    word = ''.join(word)
                    print("Great guess!")
                    print("Congratulations, you figured it out!\n")
                    print(f'{word} is the word' + "\n")
                    saved += 1
                    break
                elif result == hidden_word:
                    hidden_word = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print(f'Good guess, {guess} is in the word.' + "\n")
                    if len(tries) > 0:
                        print("Failed guesses: "+(' '.join(tries)).upper())
        if end_game(saved, killed):
            break


main()
