import random

words = ["python", "hangman", "guitar", "jungle", "rocket"]

def get_word():
    word = random.choice(words)
    return word

def play():
    word = get_word()
    guessed = []
    wrong = []
    attempts = 6

    print("\nLet's play Hangman!")
    print("The word has", len(word), "letters\n")

    while attempts > 0:
        # show the word with blanks
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("Word:", display)
        print("Wrong guesses:", wrong)
        print("Attempts left:", attempts)

        # check if won
        if "_" not in display:
            print("\nYou guessed it! The word was:", word)
            return

        guess = input("\nGuess a letter: ").lower()

        # basic input check
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only")
            continue

        if guess in guessed or guess in wrong:
            print("You already tried that letter!")
            continue

        if guess in word:
            guessed.append(guess)
            print("Good guess!")
        else:
            wrong.append(guess)
            attempts -= 1
            print("Wrong! -1 attempt")

            # draw the hangman step by step
            if attempts == 5:
                print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========""")
            elif attempts == 4:
                print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
            elif attempts == 3:
                print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")
            elif attempts == 2:
                print("""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""")
            elif attempts == 1:
                print("""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""")
            elif attempts == 0:
                print("""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""")
                print("\nGame over! The word was:", word)
                return

# run the game
while True:
    play()
    again = input("\nPlay again? (y/n): ")
    if again != "y":
        print("Thanks for playing!")
        break
