#!/usr/bin/env python3

"""Script of the 'Brain-Prime' game."""

from brain_games import game_engine, games


def main():
    """Start the 'Brain-Prime' game."""
    game_engine.play_game(games.brain_prime_game)


if __name__ == '__main__':
    main()
