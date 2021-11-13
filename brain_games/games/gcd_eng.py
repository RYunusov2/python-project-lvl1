#!/usr/bin/env python3

from random import randint
from brain_games.games.q_a import quest_ans
from math import gcd


def find_gcd(name):
    print('Find the greatest common divisor of given numbers.')
    n = 1
    while n <= 3:
        number_one = randint(0, 100)
        number_two = randint(0, 100)
        print('Question: ' + str(number_one) + ' ' + str(number_two))
        cor_ans = str(gcd(number_one, number_two))
        n = quest_ans(name, cor_ans, n)
