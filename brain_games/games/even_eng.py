#!/usr/bin/env python3

from random import randint
from brain_games.games.q_a import quest_ans


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')
    n = 1
    while n <= 3:
        number = randint(0, 100)
        print('Question:', number)
        if number % 2 == 0:
            cor_ans = 'yes'
        else:
            cor_ans = 'no'
        n = quest_ans(name, cor_ans, n)
