class SpatioTemporalData(object):
    def __init__(self, data):
        self.data = data

    def when(self, location):
        try:
            is_locate = self.data[self.data['City'] == location]
            values = is_locate['Year'].unique()
            result = [int(date) for date in values]
            return result
        except Exception as e:
            print(f'Exception: {type(e).__name__} -- {e}')

    def where(self, date):
        try:
            is_this_date = self.data[self.data['Year'] == date]
            values = is_this_date['City'].unique()
            return str(values[0])
        except Exception as e:
            print(f'Exception: {type(e).__name__} -- {e}')
