import pandas as pd


class DataManager(object):
    def __init__(self,config,data_file_path):
        self.config = config
        self.data_file_path = data_file_path

