word_list = ["aardvark", "baboon", "camel"]
import random as rand


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = rand.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in chosen_word:
    if guess == i:
       print("Right")
    else:
       print("Wrong")