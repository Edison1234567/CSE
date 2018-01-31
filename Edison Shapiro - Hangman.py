import random
"""
This is a guide of how to
make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Add user input to a list of letters_guessed
4. Reveal Letters based on input
5. Create win and lose conditions
"""
guesses_left = 10
# Adding things to a list
word_bank = ['pokemon', "polygons", "football", "volleyball", "basketball", "tennis", "soccer", "computer", "justice",
             "tigers"]
the_answer = random.choice(word_bank)
guess = "*"
letters_guessed = []
while guess != 'quit':
    output = []
    for letter in the_answer:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    guess = input("Guess a letter: ")
    if guess in the_answer:
        print("you have won this guess")
    else:
        print("wrong guess try again")
        guesses_left -= 1
    letters_guessed.append(guess)
    print(letters_guessed)
    if int(10):
        
            print("guesses are used game over")