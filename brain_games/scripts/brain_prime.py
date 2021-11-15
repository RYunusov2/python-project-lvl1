#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.prime_eng import is_prime


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    is_prime(name)


if __name__ == '__main__':
    main()
