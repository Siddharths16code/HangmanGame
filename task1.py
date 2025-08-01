# codealpha : task 1 : hangman game  


import random  # Step 1: Import the random module to randomly choose a word

# Step 2: Define the Hangman game logic inside a function
def hangman_game():
    # Step 3: Welcome message
    print("🎯 Welcome to the Hangman Game!")
    print("Guess the word one letter at a time.")
    print("You have only 6 chances to make mistakes. Let's begin!\n")

    # Step 4: Create a predefined list of 5 words
    word_list = ["python", "apple", "india", "laptop", "human"]
    
    # Step 5: Randomly select one word as the secret word
    secret_word = random.choice(word_list)

    # Step 6: Initialize guessed letters list and chances
    guessed_letters = []
    attempts_left = 6

    # Step 7: Display underscores for unguessed letters
    display_word = ["_" for _ in secret_word]

    # Step 8: Start the main game loop
    while attempts_left > 0:
        # Show the current progress of the word
        print("Word:", " ".join(display_word))
        print(f"Mistakes left: {attempts_left}")
        
        # Step 9: Take input from the user
        guess = input("Guess a letter: ").lower().strip()

        # Step 10: Validate the input
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter only.\n")
            continue

        # Step 11: Check if letter was already guessed
        if guess in guessed_letters:
            print("😅 You've already guessed that letter. Try something else.\n")
            continue

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # Step 12: Check if guessed letter is in the secret word
        if guess in secret_word:
            print("✅ Good job! That letter is in the word.\n")
            # Replace underscore with correct letter in all positions
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            attempts_left -= 1
            print("❌ Oops! That letter is not in the word.\n")

        # Step 13: Check if the player has guessed all letters
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        # Step 14: If all chances used, game over
        print("😢 You've used all your chances. The word was:", secret_word)

# Step 15: Run the game function
hangman_game()
