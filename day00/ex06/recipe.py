#! /usr/bin/env python3
def add_recipe(cookbook):
	print("Please enter the recipe's name")
	name = input()
	print("Please enter type of recipe")
	meal = input()
	print("Please enter ingredients separated by commas")
	ingredients = input().split(',')
	for each in ingredients:
		each = each.strip()
	print("Please enter preparation time in minutes")
	prep = input()

	cookbook[name] = {
		"ingredients": ingredients,
		"meal": meal,
		"prep_time" : prep
		}
	print("Recipe", name, "added.\n")
	return cookbook

def recipe_tostr(cookbook, name):
	print("Name:", name)
	print("Meal:", cookbook[name]['meal'])
	print("Ingredients: ", end='')
	for ingredient in cookbook[name]['ingredients']:
		print(ingredient, end='')
		if ingredient != cookbook[name]["ingredients"][-1]:
			print(", ", end='')
		else:
			print()
	print("Prep time:", cookbook[name]['prep_time'], "minutes\n")

def find_recipe(cookbook):
	name = input("Write the name of the recipe to search: ")
	for each in cookbook:
		if each == name:
			recipe_tostr(cookbook, name)
			return
	print("No recipes found for that search")
	return
				
def delete_recipe(cookbook):
	name = input("Write the recipe to delete: ")
	for each in cookbook:
		if each == name:
			del cookbook[name]
			return
	print("That recipe doesn't exist in this cookbook.")

def print_cookbook(cookbook):
	for each in cookbook:
		recipe_tostr(cookbook, each)


def main():
	cookbook = {
		"sandwich" : 
		{
			"ingredients" :	(["ham", "bread", "cheese", "tomatoes"]),
			"meal" : "lunch",
			"prep_time" : "10"
		},
		"cake" : 
		{
			"ingredients" :	(["flour", "sugar", "eggs"]),
			"meal" : "dessert",
			"prep_time" : "60"
		},
		"salad" : 
		{
			"ingredients" :	(["avocado", "arugula", "tomatoes", "spinach"]),
			"meal" : "lunch",
			"prep_time" : "15"
		}
	}

	while (1):
		print("Please select an option by typing the corresponding number:")
		print("1: Add a recipe")
		print("2: Delete a recipe")
		print("3: Print a recipe")
		print("4: Print the cookbook")
		print("5: Quit")
		x = input()
		if x == "1":
			cookbook = add_recipe(cookbook)
		elif x == "2":
			delete_recipe(cookbook)
		elif x == "3":
			find_recipe(cookbook)
		elif x == "4":
			print_cookbook(cookbook)
		elif x == "5":
			exit()
		else:
			print("This option doesn't exist, please type the corresponding number.\n")
if __name__ == "__main__":
	main()