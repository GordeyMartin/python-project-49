#!/usr/bin/env python3
import random
import sys
import math
from brain_games import cli
from brain_games import game_system
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")

def main():
    def is_prime(a):
        if a % 2 == 0:
            return a == 2
        d = 3
        while d * d <= a and a % d != 0:
            d += 2
        return d * d > a

    cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:
        num = random.randint(0,40)
        question = str(num)
        
        if is_prime(num) == True:
            r_answer = "yes"
        else:
            r_answer = "no"

        count = game_system.game_sys(count,question,r_answer)
    print(f'Congratulations, {cli.name}')


if __name__ == '__main__':
    main()
