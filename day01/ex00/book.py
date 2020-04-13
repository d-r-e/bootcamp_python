# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/10 11:51:51 by darodrig          #+#    #+#              #
#    Updated: 2020/04/10 11:51:51 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from datetime import datetime

class Book(object):
	def __init__(self, name, recipes_list):
		self._name = name
		self._last_update = datetime.now()
		self._creation_date = datetime.now()
		self._recipes_list = recipes_list

	def get_recipe_by_name(self, value):
		for each in self._recipes_list.values():
			for recipe in each:
				if recipe._name == value:
					print(str(recipe))
					return
		print("Recipe not found.")
	
	def get_recipes_by_types(self, recipe_type):
		if recipe_type in ['starter', 'lunch', 'dessert']:
			for each in self._recipes_list[recipe_type]:
				self.get_recipe_by_name(each._name)
				print()
			return
		print("Invalid type.")

	def add_recipe(self, recipe):
		if type(recipe) is not Recipe:
			print("Invalid recipe")
			return
		if recipe._recipe_type not in self._recipes_list.keys():
			print("Invalid type")
			return
		self._recipes_list[recipe._recipe_type].append(recipe)
		self._last_update = datetime.now()