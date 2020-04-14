#!/usr/bin/env python3
from eval import Evaluator

def main():
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1, 2, 1, 4, 0.5]

	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))
if __name__ == '__main__':
	main()
	