#!/usr/bin/env python3
import random
import sys
from brain_games import cli
sys.path.append("python-project-49/brain_games")
sys.path.append("brain_games")

def main():
	def ifeven(num):
		if num % 2 == 0:
			return 'yes'
		else:
			return 'no'
	name = cli.welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')

	count = 0
	while count < 3:
		number = random.randint(1,40)
		print(f'Question: {number}')
		u_answer = input('Your answer: ')
		r_answer = ifeven(number)
		if u_answer == r_answer:
			count += 1
			print('Correct!')
	print(f'Congratulations, {name}')


if __name__ == '__main__':
	main()
