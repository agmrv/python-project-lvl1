"""'Brain-Progression' game logic."""

from random import randint

RULES = 'What number is missing in the progression?'


def get_progression(step, hidden_num_index):
    """Get the progression.

    Args:
        step: progression step
        hidden_num_index: hidden num index

    Returns:
        return question and correct_answer
    """
    first_num = randint(1, 10)
    iteration = 0
    progression = ''
    correct_answer = 0
    length_of_progression = 10

    while iteration < length_of_progression:
        if iteration == hidden_num_index:
            correct_answer += first_num
            progression = '{0}{1}'.format(progression, '.. ')
            iteration += 1
            first_num += step
        else:
            progression = '{0}{1}{2}'.format(progression, str(first_num), ' ')
            iteration += 1
            first_num += step

    return progression[:-1], str(correct_answer)


def start_game():
    """Start the 'Brain-Progression' game.

    Returns:
        return the question and correct_answer.
    """
    step = randint(1, 10)
    hidden_num_index = randint(0, 9)

    return get_progression(step, hidden_num_index)
