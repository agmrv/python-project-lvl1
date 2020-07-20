"""'Brain-GCD' game logic."""

from random import randint

RULES = 'Welcome to the Brain Games!\nFind the greatest common divisor of given numbers.\n'


def gcd(num1, num2):
    """Get the GCD of num1 and num2.

    Args:
        num1: The first num.
        num2: The second num.

    Returns:
        return the GCD.
    """
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def start_game():
    """Start the 'Brain-GCD' game.

    Returns:
        return the question and correct_answer.
    """
    num1 = randint(2, 100)
    num2 = randint(2, 100)
    question = '{0} {1}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
