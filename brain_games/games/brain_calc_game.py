"""'Brain-Calc' game logic."""

from random import choice, randint

RULES = 'What is the result of the expression?'

operators = ('+', '-', '*')


def start_game():
    """Start the 'Brain-Calc' game.

    Returns:
        return the question and correct_answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    current_operator = choice(operators)
    question = '{0} {1} {2}'.format(num1, current_operator, num2)

    if current_operator == '+':
        correct_answer = str(num1 + num2)
    elif current_operator == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)

    return question, correct_answer
