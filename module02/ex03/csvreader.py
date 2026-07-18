class CorruptedFileError(Exception):
    pass


class CsvReader():
    def __init__(self, filename=None, sep=',', header=True, skip_top=1,
                 skip_bottom=1):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = 0
        self.elements = []

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            elements = self.file.readlines()
            elements = [el.strip('\n') for el in elements]
            self.elements = [el.split(self.sep) for el in elements]
            lengths = [len(el) for el in self.elements]
            if len(set(lengths)) != 1:
                raise CorruptedFileError('The file is corrupted, differents'
                                         'number of values in line.')
        except Exception:
            return None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return None

    def getdata(self):
        """ Retrives the data/records from skip_top to skip bottom.
            Returns:
                nested list (list(list, list, ...)) representing data.
        """
        b = 0
        e = len(self.elements)
        if self.skip_top:
            b = 1
        if self.skip_bottom:
            e = e - 1
        return self.elements[b:e]

    def getheader(self):
        """ Retrives the header from the csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header is True:
            return self.elements[0]
        else:
            return None
