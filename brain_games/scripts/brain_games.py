#!/usr/bin/env python3
from brain_games.cli import welcome_user,name
from brain_games.scripts.brain_even import parity


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    welcome_user()
    parity()


if __name__ == '__main__':
    main()
