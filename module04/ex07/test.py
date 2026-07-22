from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module04/attachments/athlete_events.csv')


from Komparator import Komparator

komp = Komparator(data)

#komp.compare_box_plots('Sex', ['Height', 'Weight'])
#komp.density('Sex', ['Height', 'Weight'])
komp.compare_histograms('Sex', ['Height', 'Weight'])
