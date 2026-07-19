import random

words = ["python", "apple", "computer", "keyboard", "hangman"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

if attempts == 0:
    print("\n💀 Game Over! The word was:", word)