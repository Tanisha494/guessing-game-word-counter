
import random
import string


# -------------------------------
# NUMBER GUESSING GAME
# -------------------------------

def guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100!")

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
                score -= 10

            elif guess > secret_number:
                print("Too high! Try again.")
                score -= 10

            else:
                print("\nCongratulations! You guessed it!")
                print("Secret number:", secret_number)
                print("Attempts:", attempts)
                print("Your score:", max(score, 0))
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# -------------------------------
# WORD FREQUENCY COUNTER
# -------------------------------

def word_counter():
    print("\n===== WORD FREQUENCY COUNTER =====")

    filename = input("Enter text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        # Remove punctuation
        words = text.translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        if not words:
            print("The file is empty or contains no words.")
            return

        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        sorted_words = sorted(
            word_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nMost Common Words:")
        for word, count in sorted_words[:10]:
            print(f"{word}: {count}")

        print("\nTotal words:", len(words))

    except FileNotFoundError:
        print("File not found! Please check the file name.")

    except OSError as error:
        print("Could not read the file:", error)


# -------------------------------
# MAIN MENU
# -------------------------------

def main():
    while True:
        print("\n==============================")
        print("       PYTHON TOOLKIT")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Word Frequency Counter")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using Python Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
