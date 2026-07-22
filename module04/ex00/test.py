from FileLoader import FileLoader


loader = FileLoader()
data = loader.load("/home/sonOfMaaJo/42/bootcamp_python/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv")

loader.display(data, 12)
print(data.columns)
print(data['Sex'])
