from random import randint
from brain_games.games.q_a import quest_ans


def prog_game(name):
    print('What number is missing in the progression?')
    n = 1
    while n <= 3:
        first = randint(0, 100)
        index = randint(-10, 10)
        progr = [first]
        m = 1
        while m <= 10:
            next = first + index
            progr.append(next)
            first = next
            m += 1
        random_index = randint(0, 9)
        cor_ans = str(progr[random_index])
        progr[random_index] = '..'
        i = 0
        output = ''
        while i <= 9:
            if output:
                output = output + ' ' + str(progr[i])
                i += 1
            else:
                output = str(progr[i])
                i += 1
        print('Question: ' + output)
        n = quest_ans(name, cor_ans, n)
