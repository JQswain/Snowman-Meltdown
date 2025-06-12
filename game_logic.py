import random
import ascii_art
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
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
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    mistake_counter = 0
    guessed_letters = []
    while mistake_counter < 3:
        display_word = display_game_state(mistake_counter, secret_word, guessed_letters)
        if display_word.replace(' ', '') == secret_word:
            print("Congratulations! You guessed the secret word!")
            break
        elif mistake_counter == 3:
            print("Sorry, the Snowman Melted")
            break
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess not in guessed_letters:
            print("You guessed:", guess)
        if guess not in secret_word:
            mistake_counter += 1
        if guess in secret_word:
            guessed_letters.append(guess)
        if mistake_counter == 3:
            print("Sorry, the Snowman Melted")
            break
    print("Thank you for playing!")

