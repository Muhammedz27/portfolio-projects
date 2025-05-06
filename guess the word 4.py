import random  # Import the random module

# List of possible secret words
words = ["technology", "chatbot", "resume", "website", "router", "switch", "laptop", "code"]

# Choose a random word from the list
secret_word = random.choice(words)

# Create the initial dashes string
dashes = "-" * len(secret_word)

# Function to retrieve a valid guess from the user
def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) == 1 and guess.islower():
            return guess
        else:
            print("Invalid input. Please enter exactly one lowercase letter.")

# Function to update the dashes based on the guess
def update_dashes(secret_word, current_dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += current_dashes[i]
    return result

# Main game function
def play_game():
    global dashes
    guesses_left = 10

    while dashes != secret_word and guesses_left > 0:
        print("\nCurrent word:", dashes)
        print("Incorrect guesses left:", guesses_left)
        guess = get_guess()

        if guess in secret_word:
            print(f"Yes! The letter '{guess}' is in the secret word.")
        else:
            print(f"Nope! The letter '{guess}' is not in the secret word.")
            guesses_left -= 1

        dashes = update_dashes(secret_word, dashes, guess)

    # End of game: win or lose
    if dashes == secret_word:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nYou lose. The word was:", secret_word)

# Start the game
play_game()
