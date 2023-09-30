#!/usr/bin/env python3
import sys
from brain_games import cli
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")


def game_sys(number, q, right):
    print(f"Question: {q}")
    u_answer = input('Your answer: ')
    if u_answer == right:
        number += 1
        print('Correct!')
        return number
    else:
        print(f"'{u_answer}' is wrong answer ;(. Correct answer was '{right}’.")
        print(f"Let's try again, {cli.name}!")
        number = 0
        exit()
        return number
