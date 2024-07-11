'''
This file runs the Gower's Distance function on the cleaned data and returns a distance matrix.
'''

import numpy as np
import gower
import pandas as pd


def similarity_matrix(df):
    '''
    Runs Gower's Distance on the cleaned data and returns a distance matrix.
    :param df: pandas dataframe
    :return: numpy array
    '''
    gower_dist = gower.gower_matrix(df)
    df_gower = pd.DataFrame(gower_dist, columns=df.index, index=df.index)
    np.fill_diagonal(df_gower.values, 10)
    df_gower = df_gower.round(4)
    return df_gower
