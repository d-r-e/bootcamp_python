#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 12:26:25 by darodrig          #+#    #+#              #
#    Updated: 2020/04/13 12:26:25 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter(object):
	def __init__(self, first_name, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good"""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name, is_alive = is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
	
	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		self.is_alive = False

