#! /usr/bin/env python3

def main():
	tup = (0, 4, 132.42222, 10000, 12345,67)
	print("day_"+ str(tup[0]).zfill(2), end=', ')
	print("ex_" + str(tup[1]).zfill(2), end=' : ')
	print(str(round(tup[2], 2)), end=', ')
	print(format(tup[3], ".2e"), end=', ')
	print(format(tup[4], ".2e"))

if __name__ == "__main__":
	main()