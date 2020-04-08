#! /usr/bin/env python3

def main():
	languages = {
  		"Python": "Guido van Rossum",
  		"Ruby": "Yukihiro Matsumoto",
		"PHP": "Rasmus Lerdorf"
	}

	for each in languages:
		print (each, end='')
		print(" was created by ", end='')
		print(languages[each])

if __name__ == "__main__":
	main()