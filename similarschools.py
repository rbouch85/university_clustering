'''
This file uses the Gower's Distance matrix to create a new dataset with the top ten 
most similar schools to a given school.
'''

import pandas as pd


def create_similar_colleges(df):
    '''
    This function takes a Gower's Distance matrix and returns a new dataset with the 
    top ten most similar schools to a given school.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    new_columns = ['input_school',
                'similar1', 
                'similar2', 
                'similar3', 
                'similar4', 
                'similar5', 
                'similar6', 
                'similar7', 
                'similar8', 
                'similar9', 
                'similar10']
    df_similar = pd.DataFrame(columns=new_columns)

    colleges = df.index.tolist()

    for college in colleges:
        topsimilar = df.sort_values(college, ascending=True).head(10)
        similar_colleges = topsimilar.index.tolist()
        similar_colleges.insert(0, college)
        df_similar.loc[len(df_similar)] = similar_colleges

    return df_similar
