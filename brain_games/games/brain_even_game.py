"""'Brain-Even' game logic."""

from random import randint

RULES = 'Welcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".\n'


def start_game():
    """Start the 'Brain-Even' game.

    Returns:
        return the question and correct_answer.
    """
    question = randint(1, 100)
    correct_answer = 'no'

    if question % 2 == 0:
        correct_answer = 'yes'

    return question, correct_answer
