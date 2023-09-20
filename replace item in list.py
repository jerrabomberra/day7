# replace item in list

import random

word_list = ["aardvark", "baboon", "camel","monkey","elephant"]
#Step 2

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
display =[]
for i in chosen_word:
    display.append('_')
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
print(display)

guess = input("Guess a letter: ").lower()
 
for idx, item in enumerate(chosen_word):
    if item==guess:
        display[idx]=item
        print(display)

