'''
This file takes a school as input and returns the top 10 most similar schools based on Gower's distance.
'''

def find_similar_top10(df_gower, college_name):
    '''
    Returns the top 10 most similar schools based on Gower's distance.
    :param df_gower: pandas dataframe
    :param college_name: str
    :return: pandas series
    '''
    college_index = df_gower.index.get_loc(college_name)
    college_row = df_gower.iloc[college_index]
    similar_colleges = college_row.nsmallest(11)
    return similar_colleges
