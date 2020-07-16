#!/usr/bin/env python3

"""Script of the 'Brain even' game."""

from brain_games.brain_even_game import start_even_game, welcome_to_even_game


def main():
    """Start the 'Brain Even' game."""
    welcome_to_even_game()
    start_even_game()


if __name__ == '__main__':
    main()
