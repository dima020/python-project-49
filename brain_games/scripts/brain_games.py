#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import parity
from brain_games.scripts.brain_calc import expression
from brain_games.scripts.brain_gcd import game_nod
from brain_games.scripts.brain_progression import brainprogression

def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name=welcome_user()
    brainprogression(name)


if __name__ == '__main__':
    main()
