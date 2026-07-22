from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')


from MyPlotLib import MyPlotLib

ploter = MyPlotLib()
#ploter.histogram(data, ['Height', 'Weight'])
#ploter.density(data, ['Height', 'Weight', 'City'])

ploter.box_plot(data, ['Height', 'Weight'])

ploter.pair_plot(data, ['Height', 'Weight'])
