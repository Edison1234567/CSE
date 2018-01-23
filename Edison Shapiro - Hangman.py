"""
This is a guide of how to
make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Hide the word (use *)
4. Reveal Letters based on input
5. Create win and lose conditions
"""
# Adding things to a list
word_bank = ['Pokemon', "Polygons", "FootBall", "VolleyBall", "BasketBall", "Tennis", "Soccer", "Computer", "Justice",
             "Tigers"]
import random  # this should be on line 1
print(random.randint(1,10))
print(word_bank[5])
