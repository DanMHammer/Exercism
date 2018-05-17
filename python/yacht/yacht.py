# Score categories
# Calling as lambda functions for efficiency and consistency
YACHT = lambda dice: 50 if sum([1 for x in dice if dice.count(x) == 5]) == 5 else 0
ONES = lambda dice: sum([1 for x in dice if x == 1])
TWOS = lambda dice: sum([2 for x in dice if x == 2])
THREES = lambda dice: sum([3 for x in dice if x == 3])
FOURS = lambda dice: sum([4 for x in dice if x == 4])
FIVES = lambda dice: sum([5 for x in dice if x == 5])
SIXES = lambda dice: sum([6 for x in dice if x == 6])
FULL_HOUSE = lambda dice: sum(dice) if sum([1 for x in dice if dice.count(x) == 3 or dice.count(x) == 2]) == 5 else 0
#Sum up the dice if there are 4 or 5 of them. Slice only the first 4 to deal with condition of 5 repeats.
FOUR_OF_A_KIND = lambda dice: sum([x for x in dice if dice.count(x)>=4][:4])
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    validation(dice)
    return category(dice)

def validation(dice):
    if not isinstance(dice, list):
        raise TypeError("Input is not a list.")
    for die in dice:
        if die not in [1,2,3,4,5,6]:
            raise ValueError("Input contains illegal character {die}.")
        elif len(dice) != 5:
            raise ValueError("Input cointains {len(dice)} dice instead of the required 5.")
