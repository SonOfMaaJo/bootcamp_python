from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')


from HowManyMedalsByCountry import how_many_medals_by_country

print(data['Team'].head())

print(how_many_medals_by_country(data, 'Argentina'))
