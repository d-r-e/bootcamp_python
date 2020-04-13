#!/usr/bin/env python3

from recipe	import	Recipe
from book	import	Book

if __name__ == "__main__":
	macncheese = Recipe("Mac'n cheese", 1, 20, ['pasta', 'cheese'], "lunch","Pretty basic")
	bolognese = Recipe("Bolognese", 2, 30, ['pasta', 'sauce'], "lunch")
	donut = Recipe("Donut", 3, 45, ['eggs', 'flour'], "dessert", "Classical recipe")
	thebook = Book("The book", {'starter':[], 'lunch': [], 'dessert':[]})
	thebook.add_recipe(donut)
	thebook.add_recipe(macncheese)
	thebook.add_recipe(bolognese)

	print("SEARCHING for Donut:")
	thebook.get_recipe_by_name("Donut")
	print()
	print("SEARCHING for Mac'n cheese")
	thebook.get_recipe_by_name("Mac'n cheese")
	print()
	print("PRINTING ALL LUNCHES")
	thebook.get_recipes_by_types("lunch")