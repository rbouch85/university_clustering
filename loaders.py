'''
This file loads data from csv files and returns a pandas dataframe.
'''

import pandas as pd

def load_data(file_path):
    '''
    :param file_path: path to the csv file
    :return: pandas dataframe
    '''
    data = pd.read_csv(file_path)
    return data
