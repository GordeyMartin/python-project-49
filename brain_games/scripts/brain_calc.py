#!/usr/bin/env python3
import random
import sys
from brain_games import cli
from brain_games import game_system
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")


def main():
    cli.welcome_user()
    print('What is the result of the expression?')

    count = 0
    while count < 3:
        f_number = random.randint(1, 40)
        s_number = random.randint(1, 40)
        op_sign = random.randint(0, 2)
        if op_sign == 0:
            r_answer = str(f_number + s_number)
            question = f"{f_number} + {s_number}"
        elif op_sign == 1:
            r_answer = str(f_number - s_number)
            question = f"{f_number} - {s_number}"
        elif op_sign == 2:
            r_answer = str(f_number * s_number)
            question = f"{f_number} * {s_number}"

        count = game_system.game_sys(count, question, r_answer)
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
