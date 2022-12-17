class SellReport:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        data_str = str(self.__dict__)
        for i in '{}\'':
            data_str = data_str.replace(i, '')
        return data_str
