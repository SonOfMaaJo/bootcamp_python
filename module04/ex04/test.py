from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')

print(data.columns)
from SpatioTemporalData import SpatioTemporalData


sp = SpatioTemporalData(data)
print(sp.where(1896))

print(sp.when('Paris'))
