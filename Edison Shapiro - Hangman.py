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
High_Score = 0
Best_round = 0
Rounds = 0
# Adding things to a list
word_bank = ['pokemon', 'polygons', 'football', 'volleyball', 'basketball', 'tennis', 'soccer', 'computer', 'justice',
             'tigers']

the_answer = random.choice(word_bank)
letters_guessed = []

while guesses_left > 0:
    output = []

    for letter in the_answer:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))

    if output == list(the_answer):
        print("You Win!")
        quit()

    guess = input("Guess a letter: ")
    if guess in the_answer:
        print("you have won this guess")
        letters_guessed.append(guess)
        print(letters_guessed)
    else:
        print("wrong guess try again")
        guesses_left -= 1
        letters_guessed.append(guess)
        print(letters_guessed)
        # print(guesses_left)
        # Describe ONE letter (This is the game's controller)
print("guesses are used game over")


