#! /usr/bin/env python3
import sys

def	main():
	usage = "Usage: python operations.py\n"\
			"Example:\n\tpython operations.py 10 3"
	if len(sys.argv) < 3:
		print(usage)
		return
	if len(sys.argv) >  3:
		print("InputError: too many numbers\n\n" + usage)
		return
	for each in sys.argv[1:]:
		for c in each:
			if c.isdigit() == 0:
				print("InputError: only numbers\n" + usage)
				return
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print("Sum:		" + str(a + b))
	print("Difference:	" + str(a - b))
	print("Product:	" + str(a * b))
	if (b == 0):
		print("ERROR (div by zero)")
		print("ERROR (modulo by zero)")
	else:
		print("Quotioent:	" + str(a / b))
		print("Remainder:	" + str(a % b))



if __name__ == "__main__":
	main()