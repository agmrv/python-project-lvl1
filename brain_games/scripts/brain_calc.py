#!/usr/bin/env python3

"""Script of the 'Brain-Calc' game."""

from brain_games import game_engine, games


def main():
    """Start the 'Brain-Calc' game."""
    game_engine.play_game(games.brain_calc_game)


if __name__ == '__main__':
    main()
