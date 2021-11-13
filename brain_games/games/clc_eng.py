#!/usr/bin/env python3

from random import randint, choice
from brain_games.games.q_a import quest_ans


def calc_game(name):
    print('What is the result of the expression?')
    n = 1
    seq = ['+', '-', '*']
    while n <= 3:
        number_one = randint(0, 10)
        number_two = randint(0, 10)
        op = choice(seq)
        print('Question: ' + str(number_one) + ' ' + op + ' ' + str(number_two))
        if op == '+':
            cor_ans = str(number_one + number_two)
        elif op == '-':
            cor_ans = str(number_one - number_two)
        else:
            cor_ans = str(number_one * number_two)
        n = quest_ans(name, cor_ans, n)
