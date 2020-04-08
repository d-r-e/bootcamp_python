#! /usr/bin/env python3

def main():
	t = (19, 42, 21)
	print("The 3 numbers are: ", end='')
	for each in t:
		print(each, end='')
		if each != t[len(t) - 1]:
			print(', ', end='')
		else:
			print()

if __name__ == "__main__":
	main()