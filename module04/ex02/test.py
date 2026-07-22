from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport


loader = FileLoader()
data = loader.load('/home/sonOfMaaJo/42/bootcamp_python/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')
print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
