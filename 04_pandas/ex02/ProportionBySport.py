from FileLoader import FileLoader
import pandas as pd

def proportionBySport(df: pd.DataFrame, year: int, sport: str, gender: str) -> float:
	all_sport_df = df[(df['Sex'] == gender) & (df['Year'] == year)]\
        .drop_duplicates(subset='Name', keep='first')
	sport_df = df[(df['Sex'] == gender) & (df['Year'] == year) & (df['Sport'] == sport)]\
        .drop_duplicates(subset='Name', keep='first')
	return sport_df['Sport'].count() / all_sport_df['Sport'].count()

	
loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
print (proportionBySport(data, 2004, 'Tennis', 'F'))