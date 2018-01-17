import random  # this should be on line 1
money = 15
High_Score = 0
Best_round = 0
Rounds = 0

while money > 0:
    print()
    print("New round")
    money -= 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(random.randint(1,6))
    print(random.randint(1,6))
    total = dice1 + dice2
    print("the total is %d" % total)
    if total == 7:
        print("You gained $5. You win this round!")
        money += 5
    else:
        print("you have lost $1. You Lose this round!")