#!/usr/bin/env python3
import random
import sys
import math
from brain_games import cli
from brain_games import game_system
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")


def main():
    cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < 3:
        f_number = random.randint(1, 40)
        s_number = random.randint(1, 40)
        question = f"{f_number} {s_number}"
        r_answer = str(math.gcd(f_number, s_number))
        count = game_system.game_sys(count, question, r_answer)
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
