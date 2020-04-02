import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ScrapBooker():
	def load(self, path):
		img = mpimg.imread(path) 
		print (f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
		return (img)
	
	def display(self, img):
		img_plot = plt.imshow(img)
		return(img_plot)

	def crop(self, array: np.array, dimensions: tuple, position = (0, 0))-> np.array:# -> np.array:
		if (dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]):
			print (f"Error: Cannot crop with dimensions ({dimensions[0]} x {dimensions[1]}) highger than the image ({array.shape[0]} x {array.shape[1]})")
			exit ()
		else:
			cropped_arr = array[position[0]: position[0] + dimensions[0],
								position[1]: position[1] + dimensions[1]]
		return cropped_arr

	def thin(self, array: np.array, n: int, axis=0) -> np.array:
		if axis == 0:
			return array[:, :n]
		elif axis == 1:
			return array[:n, :]

	def juxtapose(self, array: np.array, n: int, axis=0) -> np.array:
		if axis == 0:
			return np.tile(array, (n, 1))
		elif axis == 1:
			return np.tile(array, (1, n))

	def mosaic(self, array: np.array, dimensions: tuple) -> np.array:
		return np.tile(array, dimensions)
		
# slice : start:stop:step

## for color image : 3D ndarray of tuple (row (height) x column (width) x color (3)).

### TESTS ###
img = ScrapBooker()
arr = img.load("../boin.jpg")
img.display(arr)
plt.show()

print ("crop:")
array = img.crop(arr, (1800, 1000), (900, 2510))
print (array)
plt.imshow(array)
plt.suptitle('crop')
plt.show()

print ("thin:")
array_1 = img.thin(arr, 1500, 1)
print (array_1)
plt.imshow(array_1)
plt.suptitle('thin')
plt.show()

print ("juxtapose:")
start = time.time()
arr2 = img.juxtapose(arr, 4, 0)
end = time.time()
print (arr2)
print(f"[ exec-time = {end - start:.7f} ms ]")
plt.imshow(arr2)
plt.suptitle('juxtapose')
plt.show()

print ("mosaic:")
start = time.time()
arr1 = img.mosaic(arr, (3, 3, 1))
end = time.time()
print (arr1.shape)
print(f"[ exec-time = {end - start:.7f} ms ]")
img.display(arr1)
plt.suptitle('mosaic')
plt.show()

# numpy.s_  :  A nicer way to build up index tuples for arrays.
# np.s_[2::2] ->  slice(2, None, 2)
# slice(start, stop, step)
# >>> np.array([0, 1, 2, 3, 4])[np.s_[2::2]]   -> array([2, 4])