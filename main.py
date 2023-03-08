#!/usr/bin/env python3

from die import Die
from dice_set import DiceSet
from scoring_group import ScoringGroup

foo = ScoringGroup([Die(1), Die(1), Die(1), Die(), Die(), Die()])

print(foo)
foo.score()
print(foo.group_score)
foo.remove_dice((1,3))
print(foo)

