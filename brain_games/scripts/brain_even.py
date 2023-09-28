#!/usr/bin/env python3
import random
import sys
from brain_games import cli
from brain_games import game_system
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")

def main():
	def ifeven(num):
		if num % 2 == 0:
			return 'yes'
		else:
			return 'no'
	cli.welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')

	count = 0
	while count < 3:
		number = random.randint(1,40)
		r_answer = ifeven(number)
		count = game_system.game_sys(count,number,r_answer)
	print(f'Congratulations, {cli.name}')


if __name__ == '__main__':
	main()
