#! /usr/bin/env python

import sys


def main():
	if len(sys.argv) < 2:
		return 0
	list = sys.argv[:0:-1]
	for each in list:
		for letter in each[::-1]:
			if letter.isupper():
				sys.stdout.write(letter.lower())
			else:
				sys.stdout.write(letter.upper())
		if each != sys.argv[1]:
			sys.stdout.write(' ')
	print("")

if __name__ == "__main__":
	main()
