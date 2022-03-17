# Hangman by Jess

Hangman by Jess is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The challenge is to find out which word is hidden.
A man will be hanged step by step if you fail.

[Click here for a live version of my project](https://hangman-by-jess.herokuapp.com)

![image of mockup](/assets/images/mockup.jpg)

## How to play

The game is based on a classic game called hangman.

First the player needs to choose a theme for the word that will lead the game.

Then the player needs to make guesses to figure out the word. It is possible to guess for the full word but also single letters. If the letter or word guessed is not in the hidden word one more symbol will be displayed on the image of the hanged man. 

If the word contains the guessed letter, it will be displayed to make it easier to figure the word out.

After 7 incorrect guesses the hangman image is fully displayed and the game is lost. If all letters in the word is guessed before this, the game is won and the man never gets hanged.

## Initial plan

![image of lucidchart](/assets/images/lucidchart.jpeg)

## Features

- Display images
- Display blanks as "hidden word"
![printscreen of game board beginning](/assets/images/beginning.jpg)
- Accepts user input
    - choosing theme.
    - making guesses.
    - play again.
![printscreen of winning](/assets/images/win.jpg)
- Random word generation
    - Gets a random word matching the theme.
- maintain amount of tries
- maintain correct guesses
![printscreen of game board](/assets/images/maintain-guess.jpg)
- Input validation and error checking
    - You cannot enter the same guess twice.
    - You cannot guess for other symbols then letters.
    - You cannot guess for words longer or shorter than the played word.
    - You cannot choose a theme that is not available.
    - You cannot answer to play again with words that doesn't start with the letters y or n.
![printscreen of invalid input](/assets/images/error.jpg)
![printscreen of invalid input](/assets/images/error-2.jpg)
### Future features
- Possibility to choose level

## Testing

I have manually tested this project by doing this:
- Passing the code through the PEP8 linter.
- Added messages with ValueError for invalid inputs.
- Testing in gitpod terminal and Code Institute Heroku terminal.
    - Let different users on different screens test the game on Code Institute Heroku terminal.

### Bugs

#### Solved bugs

- After testing in Code Institute Heroku terminal I found out that some guesses never got validated as correct even if they were correct.
    - Realised that some screens put capital letters as default and that’s when the guess was not validated correctly.
        - Solved the bug by transforming all guesses to uppercase directly.

#### Remaining bugs

- On some screens the underscores in "Hidden word" is not displayed.

### Validator testing

- No errors were found when passing through [PEP8 Validator](http://www.pep8online.com/checkresult)

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.

- Deployment at regular intervals:
    - I used command git add filename to add the various files into it.
    - Then i committed to local repo with command git commit -m "useful string info".
    - Then finally uploaded it to my GitHub repo with git push.
- Final deployment in Heroku:
    - Fork github repository.
    - Create new Heroku app.
    - Set the buildbacks to Python and NodeJS in that order.
    - Link the Heroku app to the repository.
    - Enable automatic deployment.
    - Click on Deploy.

## Credits

- Code Institute for the deployment terminal.

Inspiration:
- [This youtube tutorial.](https://www.youtube.com/watch?v=m4nEnsavl6w)
- [This code.](https://inventwithpython.com/invent4thed/chapter8.html)