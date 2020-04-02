def ft_filter(function_to_apply, list_of_inputs):
	filtered_values = [item for item in list_of_inputs if function_to_apply(item)]
	return (filtered_values)

items = [1, 2, 3, 4, 5]
even = ft_filter(lambda x: x % 2 == 0, items)
print (even)

items2 = [1, 2, 3, 4, 5]
bigger_than_2 = ft_filter(lambda x: x > 2, items2)
print (bigger_than_2)
