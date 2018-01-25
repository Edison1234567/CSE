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
# Adding things to a list
word_bank = ['Pokemon', "Polygons", "FootBall", "VolleyBall", "BasketBall", "Tennis", "Soccer", "Computer", "Justice",
             "Tigers"]
the_answer = random.choice(word_bank)
print(the_answer)
guesses_left = 10
letters_guessed = []
