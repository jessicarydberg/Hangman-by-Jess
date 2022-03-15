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
    Lets the user choose a theme for words to play with.
    Picks a random word to play with and prepares for the game to start.
    """
    print("\n")
    print("Welcome to the games of HangMan!\n")
    print("You can choose between three themes: Animals, Sports or Furniture")
    themes = ["animals", "sports", "furniture"]
    while True:
        theme = input("Please enter the theme you would like to play: ")
        try:
            if theme.lower() in themes:
                break
            else:
                raise ValueError(
                    f'{theme} is not available'
                )
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again!")
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
    Lets the user make a guess, validates the input and checks
    if the guess is correct or not.
    """
    print(HANGMAN[len(tries)])
    print((' '.join(hidden_word)).upper())
    print("\n")
    if len(tries) > 0:
        print("Guessed: " + (' '.join(tries)).upper() + "\n")
    while True:
        guess = input("Please make a guess: ")
        print("\n")
        if validate_guess(guess, word, hidden_word, tries):
            break
    guess = list(guess)
    if guess == word:
        end_game("win")
    elif len(guess) > 1 and guess != word:
        collect_tries(tries, word, hidden_word, guess)
    elif guess[0] in word:
        add_letter(guess, word, hidden_word, tries)
    else:
        collect_tries(tries, word, hidden_word, guess)


def validate_guess(guess, word, hidden_word, tries):
    """
    Validates the data provided in the input for guessing.
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
                if ''.join(guess) in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
        else:
            raise ValueError(
                "Your guess needs to contain letters only"
            )
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again!")
        return False

    return True


def add_letter(guess, word, hidden_word, tries):
    """
    Collects guessed letters that are correct and adds them to the hidden word.
    """
    print("Good guess!\n")
    if hidden_word == word:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game("win")
    else:
        for i in range(len(word)):
            if word[i] == guess[0]:
                hidden_word[i] = guess[0]
    if "_" in hidden_word:
        get_guess(word, hidden_word, tries)
    else:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game("win")


def collect_tries(tries, word, hidden_word, guess):
    """
    Collects all incorrect guesses and checks if the user has any tries left.
    """
    print("Oops bad guess...\n")
    tries.append(''.join(guess))
    if len(tries) == 7:
        print("The hidden word is: " + (' '.join(word)).upper() + "\n")
        end_game("loose")
    else:
        get_guess(word, hidden_word, tries)


def end_game(result):
    """
    Prints message to inform if the game was won or lost.
    Provides a possibility to play again or end the game.
    """
    if result == "win":
        print("Hey you won the game!\n")
    elif result == "loose":
        print("...Oh no!\n")
        print("No tries left...\n")
        print("...you killed him!")
        print(HANGMAN[7] + "\n")
    while True:
        play = input("Want to play again? (Yes or No): ")
        try:
            if play.lower().startswith('y') or play.lower().startswith('n'):
                break
            else:
                raise ValueError(
                    f'{play} is not a valid input'
                )
        except ValueError as e:
            print(f'{e}. Please answer Yes or No')
    if play.lower().startswith('y'):
        print("\nAwesome, lets go!")
        main()
    else:
        print("\nThank you for playing!\n")


def main():
    tries = []
    word, hidden_word = get_word()
    get_guess(word, hidden_word, tries)


main()
