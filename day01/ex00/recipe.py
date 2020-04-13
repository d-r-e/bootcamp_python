# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@student42madrid.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/11 00:31:06 by darodrig          #+#    #+#              #
#    Updated: 2020/04/11 00:31:06 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe(object):
	def __init__ (self, name, cooking_lvl, \
            cooking_time, ingredients, recipe_type, description=""):
		self._name = name
		self._cooking_lvl = cooking_lvl
		if self._cooking_lvl not in range(1, 7):
			raise Exception("Level must be from 1 to 6")
		self._cooking_time = cooking_time
		self._ingredients = ingredients
		self._recipe_type = recipe_type
		if self._recipe_type not in ['starter', 'lunch', 'dessert']:
			raise Exception("Type must be starter, lunch or dessert")
		self._description = str(description)

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ""
		txt += "Name: " + self._name
		txt += "\nCooking Level: " + str(self._cooking_lvl)
		txt += "\nCooking Time: " + str(self._cooking_time) + " minutes"
		txt += "\nIngredients: "
		txt += ", ".join(self._ingredients)
		txt += "\nRecipe type: " + self._recipe_type
		if self._description:
			txt += "\nDescription: " + self._description
		return txt