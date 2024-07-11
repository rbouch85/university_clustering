'''
This file takes the cleaned dataset and performs tests to make sure all the data is complete.
Prints out the number of missing values in each column.
'''

import numpy as np


def test1(data):
    '''
    This function prints the number of missing values in the entire dataset.
    :param data: pandas dataframe
    :return: None
    '''
    print('Number of missing values in the entire dataset:')
    n1 = data.isnull().sum().sum()
    print(n1)
    if n1 == 0:
        print('PASS')
    else:
        print('FAIL')
        print('Columns with missing values:')
        print(data.columns[data.isnull().any()])


def test2(data):
    '''
    This function prints the distinct data types in the dataset.
    :param data: pandas dataframe
    :return: None
    '''
    print('Distinct data types in the dataset:')
    print(data.dtypes.unique())


def test3(data):
    '''
    This function prints the min, max, and number of missing values for numeric columns.
    It also prints the number of unique values for non-numeric columns.
    :param data: pandas dataframe
    :return: None
    '''
    for column in data.select_dtypes(include=[np.number]).columns:
        print(f'{column}: min={data[column].min()}, max={data[column].max()}')
        print(f'{column}: missing={data[column].isnull().sum()}')
    for column in data.select_dtypes(exclude=[np.number]).columns:
        print(f'{column}: unique={data[column].nunique()}')


def test4(data):
    '''
    This function checks if the index values are unique.
    :param data: pandas dataframe
    :return: None
    '''
    index_values = data.index.values
    if len(index_values) == data.index.nunique():
        print('PASS')
    else:
        print('FAIL')


def all_tests(data):
    '''
    This function runs all the tests.
    :param data: pandas dataframe
    :return: None
    '''
    test1(data)
    test2(data)
    test3(data)
    test4(data)
