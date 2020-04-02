import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from FileLoader import FileLoader

class MyPlotLib:
	
	NUMERICS = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
	
	@staticmethod
	def histogram(df, features):
		features_df = df[features].select_dtypes(include=MyPlotLib.NUMERICS).drop_duplicates()
		for feature in features_df:
			hist = df[feature].plot.hist()
			hist.set_xlabel(feature)
			plt.figure()
			hist.plot()
		plt.show()
	
	def density(self, df: pd.DataFrame, features: list):
		df[features].plot.kde()
		plt.show()
	
	def pair_plot(self, df: pd.DataFrame, features: list):
		sns.pairplot(df[features], markers=".", height=2, plot_kws=dict(linewidth=0))
		plt.show()
	
	def box_plot(self, df: pd.DataFrame, features: list):
		sns.boxplot(data=df[features])
		plt.show()

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
plot = MyPlotLib()
print ("yo")
plot.histogram(data, ["Height", "Weight"])