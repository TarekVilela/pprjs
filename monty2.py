import random

doors = [1,2,3]
no_change_wins = 0
no_change_loses = 0
change_wins = 0
change_loses = 0

foi = True
while foi:
    try:
        n = int(input('> '))
        foi = False
    except:
        print('Digite um número inteiro!')

for i in range(n):
    prize = random.choice(doors)
    choice = random.choice(doors)
    if choice == prize:
        no_change_wins += 1
    else:
        no_change_loses += 1

    prize = random.choice(doors)
    choice = random.choice(doors)
    if choice == prize:
        change_loses += 1

    elif choice != prize:
        change_wins += 1

print(no_change_wins,no_change_loses, no_change_wins/n)
print(change_wins,change_loses,change_wins/n)

