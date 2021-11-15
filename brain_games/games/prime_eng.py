from random import randint
from brain_games.games.q_a import quest_ans
import math


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 1
    while n <= 3:
        number = randint(2, 100)
        if number == 2 or number == 3:
            cor_ans = 'yes'
        elif number % 2 == 0:
            cor_ans = 'no'
        else:
            i = 3
            while i <= math.ceil(number) / 2:
                if number % i != 0:
                    cor_ans = 'yes'
                    i += 1
                else:
                    cor_ans = 'no'
                    i = number
        print('Question: ' + str(number))
        n = quest_ans(name, cor_ans, n)
