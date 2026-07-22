from FileLoader import FileLoader
from YoungestFellah import youngest_fellah


loader = FileLoader()
data = loader.load('/home/sonOfMaaJo/42/bootcamp_python/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')

print(youngest_fellah(data, 2004))
