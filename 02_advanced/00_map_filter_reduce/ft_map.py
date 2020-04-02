def ft_map(function_to_apply, list_of_inputs):
	map_values = [function_to_apply(item) for item in list_of_inputs]
	return (map_values)

dict_a = [{'name': 'python', 'version' : 3.7}, {'name': 'java', 'version': 8}]
version = ft_map(lambda x : x['version'], dict_a)
print(version)

items = [1, 2, 3, 4, 5]
plus_42 = ft_map(lambda x: x+32, items)
print (plus_42)
