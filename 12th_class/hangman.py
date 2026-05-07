# HANGMAN GAME
import random
from hangman_art import stages, welcome, congrats
from hangman_words import word_list

# word_list = ["apple", "banana", "cat"]
lives = 6

chosen_word = random.choice(word_list)

blanks = ""
word_length = len(chosen_word)

for i in range(word_length):
    blanks += "_"

print(welcome)
print(blanks)

correct_letters = []
game_on = True
while game_on:
    print(stages[lives])
    guess = input("Guess the letter: ").lower()
    # print(guess)
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display +=letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print("You have lost a life.")
        if lives == 0:
            game_on = False
            print("You lose! The man has been hung!")

    if "_" not in display:
        print("You win! You saved a life.")
        print(congrats)
        game_on = False

