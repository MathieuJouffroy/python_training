import pandas as pd

class FileLoader():

	@staticmethod
	def load(path):
		df = pd.read_csv(path)
		print ("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1])) 
		return (df)
	@staticmethod
	def display(df, n):
		print (df.head(n))
