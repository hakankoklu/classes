from itertools import *


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for d1, d2 in product(dice1, dice2):
        if d1 > d2:
            dice1_wins += 1
        elif d2 > d1:
            dice2_wins += 1

    return dice1_wins, dice2_wins


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    beatings = [0] * len(dices)
    for ind1, ind2 in combinations(range(len(dices)), 2):
        cwins = count_wins(dices[ind1], dices[ind2])
        if cwins[0] > cwins[1]:
            beatings[ind2] += 1
        elif cwins[1] > cwins[0]:
            beatings[ind1] += 1

    if 0 in beatings:
        return beatings.index(0)
    else:
        return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    is_best = find_the_best_dice(dices)

    if is_best != -1:
        strategy['first_dice'] = is_best
    else:
        strategy['choose_first'] = False
        del strategy['first_dice']
        beatings = [-1] * len(dices)
        for ind1, ind2 in combinations(range(len(dices)), 2):
            cwins = count_wins(dices[ind1], dices[ind2])
            if cwins[0] > cwins[1]:
                beatings[ind2] = ind1
            elif cwins[1] > cwins[0]:
                beatings[ind1] = ind2
        for ind in range(len(dices)):
            strategy[ind] = beatings[ind]

    return strategy


# print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
# print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))
# print(compute_strategy([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]))
