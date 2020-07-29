"""'Brain-Even' game logic."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_game_data():
    """Generate the 'Brain-Even' data.

    Returns:
        return the question and correct_answer.
    """
    question = randint(1, 100)
    correct_answer = 'no'

    if question % 2 == 0:
        correct_answer = 'yes'

    return question, correct_answer
