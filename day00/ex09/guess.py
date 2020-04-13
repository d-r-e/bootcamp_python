#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/09 16:22:11 by darodrig          #+#    #+#              #
#    Updated: 2020/04/09 16:22:11 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from random import randint

if __name__ == "__main__":
	nb = randint(1, 99)
	attempts = 0
	print("You have to enter a number between 1 and 99 to find out the",
			"secret number.\nType 'exit' to end the game.\n")
	while (1):
		print("What's your guess between 1 and 99?")
		x = input()
		if x == "exit":
			print("Goodbye!")
			exit()
		attempts += 1
		if not x.isdigit():
			print("That's not a number.")
		elif int(x) == 42:
			print("The answer to the ultimate question of life, "
				+ "the universe and everything is 42.")
			print("Congratulations! You got it on your first try!")
			exit()
		elif int(x) == nb:
			print("Congratulations, you've got it!")
			print("You won in", attempts, "attempts!")
			exit()
		elif int(x) < nb:
			print("Too low!")
		else:
			print("Too high!")

