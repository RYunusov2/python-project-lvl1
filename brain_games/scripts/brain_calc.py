#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.clc_eng import calc_game


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    calc_game(name)


if __name__ == '__main__':
    main()
