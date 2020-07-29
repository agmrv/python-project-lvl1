#!/usr/bin/env python3

"""Script of the 'Brain-Progression' game."""

from brain_games import game_engine, games


def main():
    """Start the 'Brain-Progression' game."""
    game_engine.play_game(games.brain_progression_game)


if __name__ == '__main__':
    main()
