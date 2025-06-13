import random
import ascii_art
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """This function displays the game state and returns the display word variable for use in the
    play_game function"""
    print(ascii_art.STAGES[mistakes])
    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_' + ' '
    print("Word: " + display_word)

    return display_word


def play_game():
    """Used to actually play the game, has all the inputs and variables in order for
     the game to be played and uses get_random_word and display_game_state."""
    while True:
        print("\nWelcome to Snowman Meltdown!\n")
        secret_word = get_random_word()
        mistake_counter = 0
        guessed_letters = []

        while mistake_counter < 3:
            display_word = display_game_state(mistake_counter, secret_word, guessed_letters)

            if display_word.replace(' ', '') == secret_word:
                print("Congratulations! You guessed the secret word!")
                break

            guess = input("Guess a letter: ").lower()

            if not (guess.isalpha() and len(guess) == 1):
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)
            print("You guessed:", guess, "\n")

            if guess not in secret_word:
                mistake_counter += 1

        if mistake_counter == 3:
            print("Sorry, the Snowman melted. The word was:", secret_word)

        response = input("Would you like to play again? (y/n): ").lower()
        if response != 'y':
            print("\nThank you for playing!")
            break

