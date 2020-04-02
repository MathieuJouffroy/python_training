import pandas as pd

class FileLoader():
	def load(self, path):
		df = pd.read_csv(path)
		print ("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1])) 
		return (df)
	def display(self, df, n):
		print (df.head(n))

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
loader.display(data, 50)