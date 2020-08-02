#!/usr/bin/env python3

"""Script of the 'Brain-Even' game."""

from brain_games import game_engine, games


def main():
    """Start the 'Brain-Even' game."""
    game_engine.play_game(games.gcd)


if __name__ == '__main__':
    main()
