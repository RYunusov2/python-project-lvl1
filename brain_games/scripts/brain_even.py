#!/usr/bin/env python3

import prompt
from random import randint


def even_game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    n = 1
    while n <= 3:
        number = randint(0, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            n += 1
            if n == 4:
                print('Congratulations, ' + name + '!')
                return()
        else:
            print("'" + answer + "'" + " is wrong answer ;(. Correct answer was " + "'" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            return()


def main():
    print('Welcome to the Brain Games!')
    even_game()


if __name__ == '__main__':
    main()
