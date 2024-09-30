import random
hangman_stages = [
    """
      ------
      |    |
      |    
      |    
      |    
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |    
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |    
    --------
    """
]

# Step 1: Display the game title
print("############################")
print("#         HANGMAN           #")
print("############################\n")

# Step 2: Randomly choose a word
list_of_words = ["prachiti", "flowers", "banana"]
choosen_word = random.choice(list_of_words)
display_list = ['_'] * len(choosen_word)  # Initialize display_list with underscores
end_of_game = False
lives = 6

# Print the word to guess with underscores
print(f"The word has {len(choosen_word)} letters: {' '.join(display_list)}\n")

# Step 3: Game loop
while not end_of_game:
    guess = input("Enter any letter: ").lower()  # Get user input

    # Track if the guess was correct
    correct_guess = False

    # Check if the guessed letter is in the chosen_word
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guess:
            display_list[i] = letter  # Replace the underscore with the guessed letter
            correct_guess = True  # Mark that the guess was correct

    # STEP 4: Check if guess was right or wrong and print appropriate messages
    if correct_guess:
        print(f"\nYou guessed right! Current word: {' '.join(display_list)}\n")
    else:
        lives -= 1
        print("\nWrong guess!")
        print(hangman_stages[lives])
        print(f"Lives left: {lives}\n")

        # Check if the user has lost
        if lives == 0:
            print("You lose!!! The correct word was:", choosen_word)
            end_of_game = True

    # Check if the user has won
    if "_" not in display_list:
        print("You win!!! The word was:", choosen_word)
        end_of_game = True
