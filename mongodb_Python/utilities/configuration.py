import json
from CONSTANS import ROOT_DIR


class Configuration:
    def __init__(self):
        self.__dict__.update(**self.__get_connection_data())


    @classmethod
    def __get_connection_data(cls):
        with open(f'{ROOT_DIR}/configuration.json') as f:
            data = f.read()
            dict_data = json.loads(data)
        return dict_data
