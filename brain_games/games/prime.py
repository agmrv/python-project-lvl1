"""'Brain-Prime' game logic."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Return True if number is prime otherwise False.

    Args:
        number: number

    Returns:
        return True or False
    """
    if number < 2:
        return False
    for divider in range(2, round(number / 2) + 1):  # '+ 1' for case number is 4
        if number % divider == 0:
            return False
    return True


def generate_game_data():
    """Generate the 'Brain-Prime' game data.

    Returns:
        return the question and correct_answer.
    """
    question = randint(3, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), correct_answer
