"""'Brain-Progression' game logic."""

from random import randint

DESCRIPTION = "What number is missing in the progression?"
LENGTH_OF_PROGRESSION = 10


def generate_game_data():
    """Generate the 'Brain-Progression' game data.

    Returns:
        return the question and correct_answer.
    """
    first_num = randint(1, 10)
    step = randint(1, 10)
    hidden_num_index = randint(0, LENGTH_OF_PROGRESSION - 1)
    question = ""

    for iteration in range(LENGTH_OF_PROGRESSION):

        if iteration == hidden_num_index:
            correct_answer = str(first_num + step * iteration)
            question = "{0}{1}".format(question, ".. ")
        else:
            question = "{0}{1}{2}".format(
                question, str(first_num + step * iteration), " "
            )

    return question[:-1], correct_answer
