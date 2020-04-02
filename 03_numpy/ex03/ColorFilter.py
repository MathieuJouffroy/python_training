import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ColorFilter():
    def load(self, path):
        img = mpimg.imread(path)
        print (f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
        return (img)
    
    def display(self, img):
        plt.imshow(img)
        plt.show()
    
    def _dtype_to_int(self, array):
        if array.dtype == np.float32:
            array = (array * 255).astype(np.uint8)
        if array.dtype == np.float64:
            array = (array * 255 * 255).astype(np.uint16)
        return array
    
    def invert(self, array: np.array):
        #  to invert the color of one pixel, we subtract the pixel's color values 
        #  from the maximum, 255 (8-bit number).
        return (255 - array)
    
    def to_blue(self, array: np.array) -> np.array:
        # create zero matrix
        split_img = np.zeros(array.shape, dtype="uint8")
        # assign blue channel
        split_img[:, :, 2] = array[:, :, 2]
        return split_img
    
    def to_green(self, array: np.array) -> np.array:
        # create zero matrix
        split_img = np.zeros(array.shape, dtype="uint8")
        # assign green channel
        split_img[:, :, 1] = array[:, :, 1]
        # using only * operator :
        #    array[:, :, [0, 2]] = array[:, :, [0, 2]] * 0
        #  return array[:, :, :] * [0, 1, 0]
        return split_img

    def to_red(self, array: np.array) -> np.array:
        # create zero matrix
        split_img = np.zeros(array.shape, dtype="uint8")
        # assign red channel
        split_img[:, :, 0] = array[:, :, 0]
        # using to_blue and to_green only:
        #   green = self.to_green(np.copy(array))
        #   blue = self.to_blue(np.copy(array))
        #   array[:, :, :] = array - green - blue
        return split_img
        # return array[:, :, :] * [1, 0, 0]

    def celluloid(self, array, thresh=4):
        thresholds = np.linspace(0, 255, num=thresh + 1, dtype="uint8")
        for i in range(thresh):
            array[(array >= thresholds[i]) & (array < thresholds[i+1])] = thresholds[i]
            array[(array >= thresholds[-2])] = thresholds[-1]
        return array


img = ColorFilter()
arr = img.load("../boin.jpg")
plt.suptitle('original')
img.display(arr)

arr1 = arr.copy()
start = time.time()
arr1 = img.invert(arr)
end = time.time()
print(f"invert:\t\t[ exec-time = {end - start:.7f} ms ]")
plt.suptitle('invert')
img.display(arr1)

arr2 = arr.copy()
start = time.time()
arr2 = img.to_blue(arr2)
end = time.time()
print(f"to_blue:\t[ exec-time = {end - start:.7f} ms ]")
plt.suptitle('blue filter')
img.display(arr2)

arr3 = arr.copy()
start = time.time()
arr3 = img.to_green(arr3)
end = time.time()
print(f"to_green:\t[ exec-time = {end - start:.7f} ms ]")
plt.suptitle('green filter')
img.display(arr3)

arr4 = arr.copy()
start = time.time()
arr4 = img.to_red(arr4)
end = time.time()
print(f"to_red:\t\t[ exec-time = {end - start:.7f} ms ]")
plt.suptitle('red filter')
img.display(arr4)

arr5 = arr.copy()
start = time.time()
arr5 = img.celluloid(arr5, 4)
end = time.time()
print(f"cell shade:\t[ exec-time = {end - start:.7f} ms ]")
plt.suptitle('shade')
img.display(arr5)

# A 3D array is like a stack of matrices:

# The first index, i, selects the matrix
# The second index, j, selects the row
# The third index, k, selects the column
