'''
This file takes a pandas dataframe and saves it to a csv file.
'''

def save_csv(df, filename):
    '''
    :param: df: pandas dataframe
    :param: filename: str
    :return: None
    '''
    df.to_csv(filename, index=False)
    return None
