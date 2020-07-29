"""'Brain-Progression' game logic."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_game_data():
    """Generate the 'Brain-Progression' game data.

    Returns:
        return the question and correct_answer.
    """
    length_of_progression = 10
    first_num = randint(1, 10)
    step = randint(1, 10)
    hidden_num_index = randint(0, length_of_progression - 1)
    question = ''

    for iteration in range(length_of_progression):
        element_of_progression = first_num + step * iteration

        if iteration == hidden_num_index:
            correct_answer = str(element_of_progression)
            question = '{0}{1}'.format(question, '.. ')
        else:
            question = '{0}{1}{2}'.format(question, str(element_of_progression), ' ')

    return question[:-1], correct_answer
