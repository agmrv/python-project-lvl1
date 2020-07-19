"""'Brain-GCD' game logic."""

from random import randint

RULES = 'Welcome to the Brain Games!\nFind the greatest common divisor of given numbers.\n'


def gcd(number1, number2):
    """Get the GCD of number1 and number2.

    Args:
        number1: The first num.
        number2: The second num.

    Returns:
        return the GCD.
    """
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)


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
