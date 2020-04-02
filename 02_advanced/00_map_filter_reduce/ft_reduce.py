def ft_reduce(function_to_apply, list_of_inputs):
	item = list_of_inputs[0]
	for next in list_of_inputs[1:]:
		item = function_to_apply(item, next)
	return item

xy_product = ft_reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(xy_product)

xy_sum = ft_reduce(lambda x, y: x+y, range(1,101))
print(xy_sum)
