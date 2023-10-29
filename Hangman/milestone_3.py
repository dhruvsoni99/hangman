# Ask the user to guess a letter and assign this to a variable called `guess`.
guess = input("Enter a letter: ")

# Check that the `guess` is a single alphabetical character.
while not guess.isalpha() or len(guess) != 1:
    print("Invalid letter. Please, enter a single alphabetical character.")
    guess = input("Enter a letter: ")

# If the `guess` passes the checks, break out of the loop.
else:
    break

print("You have entered a valid letter: " + guess)


# Create an if statement that checks if the guess is in the word.
if guess in word:
    # The guess is in the word
    print("Good guess! {} is in the word.".format(guess))

# Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
else:
    # The guess is not in the word
    print("Sorry, {} is not in the word. Try again.".format(guess))

def check_guess(guess):
    # Convert the guess to lower case.
    guess = guess.lower()

    # Check if the guess is in the word.
    if guess in word:
        return True
    else:
        return False

def ask_for_input():
    # Get the user's guess.
    guess = input("Enter a letter: ")

    # Check if the guess is a single alphabetical character.
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid letter. Please, enter a single alphabetical character.")
        guess = input("Enter a letter: ")

    # Call the check_guess function to check if the guess is in the word.
    if check_guess(guess):
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))

# Outside the function, call the ask_for_input function to test your code.
ask_for_input()

