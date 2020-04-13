#! /usr/bin/env python3

def main():
	t = (19, 42, 21)
	print("The 3 numbers are: "
		+ (', '.join(str(each) for each in t)))

if __name__ == "__main__":
	main()