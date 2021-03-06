#! /usr/bin/env python3

import sys

def	main():
	if len(sys.argv) == 1:
		return
	if len(sys.argv) != 2:
		print("ERROR")
		return
	if sys.argv[1][0] == '-':
		sys.argv[1] = sys.argv[1][1:]
	for each in sys.argv[1]:
		if each.isdigit() == 0:
			print("ERROR")
			return
	if sys.argv[1] == "0":
		print("I'm Zero.")
		return
	if int(sys.argv[1][-1]) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if __name__ == "__main__":
	main()