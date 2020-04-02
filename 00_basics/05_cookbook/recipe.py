cookbook = {
	'sandwich': {'ingredients' : ['ham','bread','cheese'], 'meal' : 'lunch', 'prep_time' : 10},
	'cake': {'ingredients' : ['flour','sugar','eggs'], 'meal' : 'dessert', 'prep_time' : 60},
	'salad': {'ingredients' : ['arugula','tomatoes','spinach'], 'meal' : 'lunch', 'prep_time' : 15}
}

def print_recipe(recipe):
	if recipe in cookbook:
		print("Recipe for {}".format(recipe))
		print("Ingredients list:{}".format(cookbook[recipe]['ingredients']))
		print("To be eaten for {}".format(cookbook[recipe]['meal']))
		print("Takes {} minutes for cooking.".format(cookbook[recipe]['prep_time']))
	else:
		print_recipe(input ("Please enter a valid recipe\n"))

def delete_recipe(recipe=""):
	if recipe in cookbook:
		del cookbook[recipe]
	else:
		delete_recipe(input ("Please enter a valid recipe\n"))

def add_recipe(recipe, ingredients, meal, prep_time):

	cookbook[recipe] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def	print_recipes_name(cookbook):
	print("\nRecipes:")
	for recipe in cookbook:
		print("{}".format(recipe))

def	cookbook_creation():
	print("\nPlease select an option by typing the corresponding number:")
	try:
		choice = int(input ("1: Add a recipe\n2: Delete a recipe\n"
		+ "3: Print a recipe\n4: Print the cookbook\n5: Quit\n"))
		if (choice == 1):
			add_recipe(input ("What is the name of your recipe ?\n"),\
			input ("What is your ingredient list?\n"),\
			input ("What kind of meal is it ?\n"),\
			int (input ("How much time does it take?\n")))
		elif (choice == 2):
			print_recipes_name(cookbook)
			delete_recipe(input ("\nWhich recipe would you like to remove?\n"))
			print_recipes_name(cookbook)
		elif (choice == 3):
			print_recipes_name(cookbook)
			print_recipe(input ("\nPlease enter the recipe's name to get its details:\n"))
		elif (choice == 4):
			print_recipes_name(cookbook)
		elif (choice == 5):
			return 
		else:
			print("This option does not exist.\nTo exit, enter 5.")
	except ValueError:
		print ("This option does not exist.\nPlease enter a valid number")
	cookbook_creation()


cookbook_creation()