import random

words = ["python", "apple", "banana", "computer", "gaming"]

score = 0

while True:

    word = random.choice(words)
    guessed_word = ["_"] * len(word)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n" + "=" * 40)
    print("        HANGMAN GAME")
    print("=" * 40)

    while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

        print("\nWord: ", end="")
        for letter in guessed_word:
            print(letter, end=" ")

        print("\nGuessed Letters:", guessed_letters)
        print("Wrong Guesses:", wrong_guesses, "/", max_wrong_guesses)

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct Guess!")

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

        else:
            wrong_guesses += 1
            print("Wrong Guess!")

    print("\n" + "=" * 40)

    if "_" not in guessed_word:
        print("CONGRATULATIONS!")
        print("You guessed the word:", word)
        score += 1
    else:
        print("GAME OVER!")
        print("The word was:", word)

    print("Current Score:", score)

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for playing!")
        print("Final Score:", score)
        break
