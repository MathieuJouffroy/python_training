class SetterProperty:
    def __init__(self, func, name=None, doc=None):
        self.func = func
        self.__name__ = name if name is not None else func.__name__
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        ret = self.func(obj, value)
        obj.__dict__[self.__name__] = value

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = set_name(name)
		#if not isinstance(name, str):
		#	raise TypeError("name must be set to a string")
		self.cooking_lvl = cooking_lvl
		#if not isinstance(cooking_lvl, int):
		#	raise TypeError("cooking_lvl must be set to a int")
		self.cooking_time = cooking_time
		#if not isinstance(cooking_time, int):
		#	raise TypeError("coooking_time must be set to a int")
		self.ingredients = ingredients
		#if not isinstance(ingredients, list):
		#	raise TypeError("ingredients must be set to a list")
		self.description = description
		#if not isinstance(description, str):
		#	raise TypeError("description must be set to a string")
		self.recipe_type = recipe_type
		#if not isinstance(recipe_type, str):
		#	raise TypeError("recipe_type must be set to a string")
	#@SetterProperty
	def set_name(self, value):
		if not isinstance(value, str):
			raise TypeError("Recipe.name must be an string")
	#def cooking_lvl(self, value):
	#	if not isinstance(cooking_lvl, int):
	#		raise TypeError("cooking_lvl must be set to a int")
	
	#def __str__(self):
    #"""Return the string to print with the recipe info"""
   # txt = ""
    #"""Your code goes here"""
    #return txt

re = Recipe(13, 12, 124, 12, 3, 134)

