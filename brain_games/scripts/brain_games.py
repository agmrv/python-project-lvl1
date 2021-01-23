#!/usr/bin/env python3

"""Script of 'Brain Games'."""

from brain_games.cli import welcome_user


def main():
    """Print greeting."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
