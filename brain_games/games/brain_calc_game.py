"""'Brain-Calc' game logic."""

import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

operators = ('+', '-', '*')


def generate_game_data():
    """Generate the 'Brain-Calc' game data.

    Returns:
        return the question and correct_answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    current_operator = choice(operators)
    question = '{0} {1} {2}'.format(num1, current_operator, num2)

    if current_operator == '+':
        correct_answer = operator.add(num1, num2)
    elif current_operator == '-':
        correct_answer = operator.sub(num1, num2)
    else:
        correct_answer = operator.mul(num1, num2)

    return question, str(correct_answer)
