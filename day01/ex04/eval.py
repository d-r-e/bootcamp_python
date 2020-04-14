#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 18:53:15 by darodrig          #+#    #+#              #
#    Updated: 2020/04/13 18:53:15 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #90

class Evaluator(object):
	def zip_evaluate(coefs, words):
		try:
			if len(words) != len(coefs):
				raise ValueError
			zipped = zip(words, coefs)
			ret = 0
			for w, c in zipped:
				ret += len(w) * c
			return ret
		except ValueError:
			return -1
	
	def enumerate_evaluate(coefs, words):
		try:
			if len(coefs) != len(words):
				raise ValueError
			ret = 0
			for i, word in enumerate(words):
				ret += len(word) * coefs[i]
			return ret
		except ValueError:
			return -1