#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import parity


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name=welcome_user()
    parity(name)


if __name__ == '__main__':
    main()
