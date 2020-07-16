"""'Brain-Even' game logic."""

from random import randint

import prompt


def welcome_to_even_game():
    """Print greeting and game rules."""
    print('Welcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".\n')


def start_even_game():
    """Start 'Brain-Even' game."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))

    iteration = 0

    while iteration < 3:
        number = randint(1, 100)
        correct_answer = 'no'

        if number % 2 == 0:
            correct_answer = 'yes'

        user_answer = prompt.string('Question: {0}\nYour answer: '.format(number))

        if user_answer == correct_answer:
            print('Correct!')
            iteration += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(user_answer, correct_answer, name))
            break

    if iteration == 3:
        print('Congratulations, {0}!'.format(name))
