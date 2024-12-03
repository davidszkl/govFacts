class RawData:
    '''Raw Data obtained from a DataSource'''
    def __init__(self, type: str, data: str | bool, *args, **kwargs):
        self.type = type
        self.data = data
        self.error = False