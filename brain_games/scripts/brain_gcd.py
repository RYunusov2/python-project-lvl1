#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.gcd_eng import find_gcd


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    find_gcd(name)


if __name__ == '__main__':
    main()
