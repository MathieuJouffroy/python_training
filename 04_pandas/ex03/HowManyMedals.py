from FileLoader import FileLoader
import pandas as pd

def howManyMedals(df: pd.DataFrame, name: str) -> dict:
	athlete_medals = {}
	year_medal_df = df[df['Name'] == name][['Year', 'Medal']]
	for year in year_medal_df['Year'].drop_duplicates():
		athlete_medals[year] = {
		'Gold': year_medal_df['Medal'][(year_medal_df['Year'] == year) & (year_medal_df['Medal'] == 'Gold')].count(),
        'Silver': year_medal_df['Medal'][(year_medal_df['Year'] == year) & (year_medal_df['Medal'] == 'Silver')].count(),
        'Bronze': year_medal_df['Medal'][(year_medal_df['Year'] == year) & (year_medal_df['Medal'] == 'Bronze')].count()
		}
	print (athlete_medals)
	return (athlete_medals)

def howManyMedalsByCountry(df: pd.DataFrame, country: str) -> dict:
	country_medals = {}
	df_subset = df[df['Team'] == country][['Year', 'Medal', 'Event']]
	for year in df_subset['Year'].drop_duplicates().sort_values():
		country_medals[year] = {
		'Gold': df_subset[['Medal', 'Event']][(df_subset['Year'] == year) & (df_subset['Medal'] == 'Gold')].drop_duplicates(subset='Event')['Medal'].count(),
		'Silver': df_subset[['Medal', 'Event']][(df_subset['Year'] == year) & (df_subset['Medal'] == 'Silver')].drop_duplicates(subset='Event')['Medal'].count(),
        'Bronze': df_subset[['Medal', 'Event']][(df_subset['Year'] == year) & (df_subset['Medal'] == 'Bronze')].drop_duplicates(subset='Event')['Medal'].count()
		}
	print (country_medals)
	return (country_medals)

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
howManyMedals(data, 'Kjetil Andr Aamodt')
howManyMedalsByCountry(data, "Canada")