#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from random import randint

import random

class DiceSet:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    def roll(self, n):
        for i in range(n):
            self._values.append(randint(1,6))
        return self._values
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        # See https://docs.python.org/3/library/random.html#random.randint

class AboutDiceProject(Koan):
    def test_can_create_a_dice_set(self):
        dice = DiceSet()
        self.assertTrue(dice)

    def test_rolling_the_dice_returns_a_set_of_integers_between_1_and_6(self):
        dice = DiceSet()

        dice.roll(5)
        self.assertTrue(isinstance(dice.values, list), "should be a list")
        self.assertEqual(5, len(dice.values))
        for value in dice.values:
            self.assertTrue(value >= 1 and value <= 6, "value " + str(value) + " must be between 1 and 6")

    def test_dice_values_do_not_change_unless_explicitly_rolled(self):
        dice = DiceSet()
        dice.roll(5)
        first_time = dice.values
        second_time = dice.values
        self.assertEqual(first_time, second_time)

    def test_dice_values_should_change_between_rolls(self):
        dice = DiceSet()
        results = []

        for _ in range(10):
            dice.roll(5)
            results.append(dice.values)
            
        self.assertFalse(any(result != results[0] for result in results[1:]), \
            "A roll should be different from the first roll")


        # THINK ABOUT IT:
        #
        # If the rolls are random, then it is possible (although not
        # likely) that two consecutive rolls are equal.  What would be a
        # better way to test this?

    def test_you_can_roll_different_numbers_of_dice(self):
        dice = DiceSet()

        dice.roll(3)
        self.assertEqual(3, len(dice.values))

        dice.roll(1)
        self.assertEqual(1, len(dice.values))
