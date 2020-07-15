"""CLI functions."""

import prompt


def welcome_user():
    """Ask the name and print greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
