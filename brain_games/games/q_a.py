#!/usr/bin/env python3

import prompt


def quest_ans(name, cor_ans, n):
    ans = prompt.string('Your answer: ')
    if ans == cor_ans:
        print('Correct!')
        n += 1
        if n == 4:
            print('Congratulations, ' + name + '!')
        return n
    else:
        text = ' is wrong answer ;(. Correct answer was '
        print("'" + ans + "'" + text + "'" + cor_ans + "'.")
        print("Let's try again, " + name + "!")
        n = 4
        return n
