"""'Brain Games game engine."""

import prompt


def welcome_to_brain_game(game):
    """Print greeting and game rules.

    Args:
        game: The game.
    """
    print(game.RULES)


def start_game(game):
    """Star the 'Brain Game'.

    Args:
        game: The game.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    iteration = 0

    while iteration < 3:
        question, correct_answer = game.start_game()
        user_answer = prompt.string('Question: {0}\nYour answer: '.format(question))

        if user_answer == correct_answer:
            print('Correct!')
            iteration += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(user_answer, correct_answer, name))
            break

    if iteration == 3:
        print('Congratulation, {0}!'.format(name))
