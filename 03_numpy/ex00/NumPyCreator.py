import numpy as np

class	NumPyCreator():

	def from_list(self, lst : list):
		return np.array(lst)

	def from_tuple(self, tpl: tuple):
		return np.array(tpl)

	def from_iterable(self, itr):
		return np.array(itr)

	def from_shape(self, shape, value=0):
		return np.full(shape, value)

	def random(self, shape):
		return np.random.random(shape)

	def identity(self, n):
		try:
			return np.identity(n)
		except TypeError:
			print ("TypeError: Can't convert {} object to int implicitly".format(type(n)))