#!/usr/bin/env python3
import random
import sys
from brain_games import cli
from brain_games import game_system
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")

def main():
    cli.welcome_user()
    print('What number is missing in the progression?')

    count = 0
    while count < 3:
        f_numb = random.randint(0,40)
        l_numb = [f_numb]
        step = random.randint(1,8)
        for i in range(9):
            l_numb.append(l_numb[-1]+step)

        mis = random.randint(0,9)
        l_copy = l_numb.copy()
        r_answer = str(l_copy[mis])
        l_numb[mis] = "..."

        question = ""
        for i in l_numb:
            question = question + str(i) + " "

        count = game_system.game_sys(count,question,r_answer)
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
