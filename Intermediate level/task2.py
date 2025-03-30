import random

def get_word_with_hint():
    words = {
        "sun": "A bright thing in the sky",
        "book": "You read it",
        "fish": "It swims in water",
        "car": "It has wheels and moves fast",
        "dog": "A loyal pet that barks"
    }
    word, hint = random.choice(list(words.items()))
    return word, hint

def display_hangman(tries):
    stages = [
        """
              -------
               |    |
               O    |
              /|\   |
              / \   |
                    |
        """,
        """
               ------
               |    |
               O    |
              /|\   |
              /     |
                    |
        """,
        """
               ------
               |    |
               O    |
              /|\   |
                    |
                    |
        """,
        """
               ------
               |    |
               O    |
              /|    |
                    |
                    |
        """,
        """
               ------
               |    |
               O    |
               |    |
                    |
                    |
        """,
        """
               ------
               |    |
               O    |
                    |
                    |
                    |
        """,
        """
               ------
               |    |
                    |
                    |
                    |
                    |
        """
    ]
    return stages[tries]

def hangman():
    word, hint = get_word_with_hint()
    chosen_word = ["_" for _ in word]
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    print("Welcome to Hangman!")
    print("Hint:", hint)
    print(display_hangman(tries))
    print(" ".join(chosen_word))

    while tries > 0 and "_" in chosen_word:
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word:
                print("Good guess!")
                for i, letter in enumerate(word):
                    if letter == guess:
                        chosen_word[i] = letter
                guessed_letters.add(guess)
            else:
                print("Incorrect guess!")
                tries -= 1
                guessed_letters.add(guess)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word!")
            elif guess == word:
                print("Congratulations! You guessed the word!")
                return
            else:
                print("Incorrect guess!")
                tries -= 1
                guessed_words.add(guess)
        else:
            print("Invalid input. Please enter a single letter or full word.")

        print(display_hangman(tries))
        print(" ".join(chosen_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Guessed words:", ", ".join(guessed_words))
    
    if "_" not in chosen_word:
        print("Congratulations! You won!")
    else:
        print("Game over! The word was:",word)


if __name__ == "__main__":
    hangman()