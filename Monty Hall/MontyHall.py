import random

doors = [1, 2, 3]

no_change_wins = 0
no_change_loses = 0
change_wins = 0
change_loses = 0

n = 1000000

for i in range(n):
    prize = random.choice(doors)
    choice = random.choice(doors)

    if choice == prize:
        no_change_wins += 1
        change_loses += 1

    else:
        no_change_loses += 1
        change_wins += 1