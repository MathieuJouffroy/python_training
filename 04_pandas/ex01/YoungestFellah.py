from FileLoader import FileLoader


def youngestFellah(df, year):
	ol_year = df[df['Year'].eq(year)]
	ol_year_female = ol_year[ol_year['Sex'].eq('F')]
	ol_year_male = ol_year[ol_year['Sex'].eq('M')]
	youngest_ol = {
		'Female' : ol_year_female.Age.min(),
		'Male' : ol_year_male.Age.min(),
	}
	# OR :
	#youngest_ol = {'f': df['Age'][(df['Sex'] == 'F') & (df['Year'] == year)].min(),
    #          'm': df['Age'][(df['Sex'] == 'M') & (df['Year'] == year)].min()}
	print (youngest_ol)

# age, sex, year
loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
loader.display(data, 10)
youngestFellah(data, 2004)
