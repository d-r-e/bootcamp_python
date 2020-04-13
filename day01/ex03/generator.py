#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 17:30:14 by darodrig          #+#    #+#              #
#    Updated: 2020/04/13 17:30:14 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from random import shuffle

def generator(text, sep=" ", option=None):
	try:
		words = text.split(sep)
		if option == "shuffle":
			shuffle(words)
		elif option == "ordered":
			words.sort(key=lambda words:words[0].swapcase())
		elif option != None:
			raise SyntaxError
		for each in words:
			yield each
	except TypeError:
		print("First parameter must be a string")
	except SyntaxError:
		print("Not a valid option: \"shuffle\" or \"ordered\"")
	
"""
if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text):
		print(word)
"""

"""
if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep=" ", option="suffle"):
		print(word)
"""

"""
if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep=" ", option="ordered"):
		print(word)
"""