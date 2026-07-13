import time
import random

# List of phrases
phrases = [
    "Python is the best coding language.",
    "Practice makes perfect.",
    "Coding improves logical thinking.",
    "Never stop learning.",
    "Programming is fun when you practice.",
    "Small steps lead to big success."
]

highest_wpm = 0


def calculate_accuracy(original, typed):
    """Calculate typing accuracy."""
    correct = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    accuracy = (correct / len(original)) * 100
    return round(accuracy, 2)


def count_mistakes(original, typed):
    """Count total mistakes."""
    mistakes = 0

    for i in range(min(len(original), len(typed))):
        if original[i] != typed[i]:
            mistakes += 1

    # Count extra or missing characters
    mistakes += abs(len(original) - len(typed))

    return mistakes


print("=" * 45)
print("      WELCOME TO THE TYPING SPEED TEST")
print("=" * 45)

while True:

    phrase = random.choice(phrases)
    word_count = len(phrase.split())

    print("\nType the following sentence exactly:\n")
    print(phrase)

    input("\nPress Enter to start...")

    start_time = time.time()

    attempt = input("\nStart typing:\n")

    end_time = time.time()

    time_taken = end_time - start_time

    # Prevent division by zero
    if time_taken == 0:
        time_taken = 0.01

    minutes = time_taken / 60

    wpm = round(word_count / minutes, 2)

    accuracy = calculate_accuracy(phrase, attempt)

    mistakes = count_mistakes(phrase, attempt)

    if wpm > highest_wpm:
        highest_wpm = wpm

    print("\n" + "=" * 45)
    print("             TEST RESULT")
    print("=" * 45)

    print(f"Time Taken : {round(time_taken,2)} seconds")
    print(f"Words      : {word_count}")
    print(f"Speed      : {wpm} WPM")
    print(f"Accuracy   : {accuracy}%")
    print(f"Mistakes   : {mistakes}")
    print(f"Best WPM   : {highest_wpm}")

    if attempt.strip() == phrase.strip():
        print("\n✅ Excellent! Perfect typing.")
    else:
        print("\n❌ The sentence did not match exactly.")
        print("Correct Sentence:")
        print(phrase)

    print("=" * 45)

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for playing!")
        print(f"🏆 Your Highest WPM: {highest_wpm}")
        print("Keep practicing. You'll get faster every day!")
        break