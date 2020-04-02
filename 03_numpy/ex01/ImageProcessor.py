import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
  
class ImageProcessor():
	def load(self, path):
		img = mpimg.imread(path) 
		print (f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
		return (img)
	
	def display(self, img):
		img_plot = plt.imshow(img)
		return(img_plot)

### TEST ###
imp = ImageProcessor()
arr = imp.load("../42AI.png")
imp.display(arr)
plt.show()

lum_img = arr[:, :, 0]
plt.imshow(lum_img)
plt.show()

plt.imshow(lum_img, cmap="hot")
plt.show()

imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.show()

imgplot = plt.imshow(lum_img)
plt.colorbar()
plt.show()
