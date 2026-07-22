from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')


from HowManyMedals import how_many_medals
print(how_many_medals(data, 'Kjetil Andr Aamodt'))
