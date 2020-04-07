#! /usr/bin/env python

def text_analyzer(txt = ""):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if txt=="":
		print("What is the text to analyse? ")
		text_analyzer(input())
		return
	upper = 0
	lower = 0
	punct = 0
	spces = 0

	for each in txt:
		if each.isupper():
			upper += 1
		elif each.islower():
				lower += 1
		elif each.isspace():
			spces += 1
		else:
			punct += 1
		
	print(str(upper) + " upper characters")
	print(str(lower) + " lower characters")
	print(str(punct) + " punctuation characters")
	print(str(spces) + " spaces")

"""
def main():
	print(text_analyzer.__doc__)
	text_analyzer()
	text_analyzer("Python 2.0, released 2000, introducedfeatures like List comprehensions and a garbage collectionsystem capable of collecting reference cycles.")
if __name__ == "__main__":
 	main()
"""