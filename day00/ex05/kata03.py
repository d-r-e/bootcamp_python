#! /usr/bin/env python3

def main():
	phrase = "The right format"
	print(phrase.rjust(42,'-'), end='')

if __name__ == "__main__":
	main()