import collections
import random

# function to determine probability of certain outcomes when rolling dice
def dice_sim(*args):
    rolls = 1000000
    diceRolls = {}
    dice = []
    for arg in args:
        dice.append(arg)
    for _ in range(0, rolls):
        sum = 0
        for die in dice:
            sum += random.randrange(1, die + 1)
        diceRolls[sum] = diceRolls.get(sum, 0) + 1
    orderedRolls = collections.OrderedDict(sorted(diceRolls.items()))
    print('OUTCOME\tPROBABILITY')
    for key, value in orderedRolls.items():
        print(f'{key}:\t{(value / rolls) * 100:.4f}%')

if __name__ == '__main__':
    dice_sim(20, 20, 20, 20)