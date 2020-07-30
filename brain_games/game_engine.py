"""'Brain Games game engine."""

import prompt

number_of_rounds = 3


def play_game(game):
    """Print greeting, game rules and play the 'Brain Game'.

    Args:
        game: The game.
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!\n'.format(name))
    iteration = 0

    while iteration < number_of_rounds:
        question, correct_answer = game.generate_game_data()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            iteration += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            return

    print('Congratulation, {0}!'.format(name))
