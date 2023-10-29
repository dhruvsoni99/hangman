class Hangman:

	def __init__(self, word_list, num_lives=5):
        	self.word = random.choice(word_list)
        	self.word_guessed = []
        	for letter in self.word:
            		self.word_guessed.append("_")
        	self.num_letters = len(set(self.word))
        	self.num_lives = num_lives
        	self.list_of_guesses = []

	def check_guess(self, guess):
    	# Convert the guessed letter to lower case.
    		guess = guess.lower()

    	# Check if the guess is in the word.
    		if guess in self.word:
        # The guess is in the word.
        		print("Good guess! {} is in the word.".format(guess))

        # Update the word_guessed list.
        		for i, letter in enumerate(self.word):
            			if letter == guess:
                			self.word_guessed[i] = guess

        # Reduce the number of letters left to guess.
        		self.num_letters -= 1

        # Return True if the player has won the game.
        		if self.num_lives == 0:
            			return True

    # The guess is not in the word.
    		else:
        # Reduce the number of lives remaining.
        		self.num_lives -= 1

        # Print a message saying "Sorry, {letter} is not in the word."
        		print("Sorry, {} is not in the word.".format(guess))

        # Print a message saying "You have {num_lives} lives left."
        		print("You have {} lives left.".format(self.num_lives))

        # Return False if the player has lost the game.
        		if self.num_lives == 0:
            			return False



    def ask_for_input(self):
        # Create a while loop and set the condition to True.
        while True:

            # Ask the user to guess a letter and assign this to a variable called `guess`.
            guess = input("Guess a letter: ")

            # Check if the guess is a single alphabetical character.
            if not guess.isalpha() or len(guess) != 1:
                # The guess is not a single alphabetical character.
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Check if the guess is already in the list_of_guesses.
            elif guess in self.list_of_guesses:
                # The guess is already in the list_of_guesses.
                print("You already tried that letter!")

            # The guess is a single alphabetical character and it's not already in the list_of_guesses.
            else:
                # Call the check_guess method.
                if self.check_guess(guess):
                    print("You won!")
                    return

                # Append the guess to the list_of_guesses.
                self.list_of_guesses.append(guess)

                # Break out of the while loop.
                break


