'''
This file cleans and filters the data and returns a cleaned pandas dataframe.
The data cleaning process includes:
- Excluding schools that do not report SAT scores
- Excluding schools that do not report admission rates
- Excluding schools that are not accredited
- Excluding duplicate schools
- Merging two completion percentage columns
- Replacing missing values with the imputed median column values
- Replacing numerical categorical codes with their plain language values
- Converts the row index to the school names
'''

import pandas as pd
from sklearn.impute import SimpleImputer


def drop_nulls(df):
    '''
    Filters out schools that do not report SAT scores, admission rates, or are not accredited.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df = df.dropna(subset=['ADM_RATE'])
    df = df.dropna(subset=['SAT_AVG'])
    df = df.dropna(subset=['ACCREDAGENCY'])
    df = df.drop(['ACCREDAGENCY'], axis=1) # column not used in analysis
    return df


def remove_duplicates(df):
    '''
    Identifies and removes duplicate schools from the dataframe.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    duplicate_list = df[df.duplicated(subset=['INSTNM'], keep=False)]['INSTNM'].tolist()
    df = df[~df['INSTNM'].isin(duplicate_list)]
    return df


def merge_columns(df):
    '''
    Merges the two completion percentage columns into one column.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df['PERCOMP'] = df[['C150_4', 'C150_L4']].max(axis=1)
    df = df.drop(columns=['C150_4', 'C150_L4'])
    return df


def fix_multitype_columns(df):
    '''
    Converts the DEBT_MDN column to a float type and removes some of the 
    unknown non-numeric entries.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df['DEBT_MDN'] = pd.to_numeric(df['DEBT_MDN'], errors='coerce')
    df['DEBT_MDN'] = df['DEBT_MDN'].astype(float)
    return df


def update_school_size(df):
    '''
    Converts the CCSIZSET column to a plain language string.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df['CCSIZSET'] = df['CCSIZSET'].astype(int)
    list_values1 = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    text_values1 = ['Not applicable', 
                'Not classified', 
                'Two-year, very small', 
                'Two-year, small', 
                'Two-year, medium', 
                'Two-year, large', 
                'Two-year, very large', 
                'Four-year, very small, primarily nonresidential', 
                'Four-year, very small, primarily residential', 
                'Four-year, very small, highly residential', 
                'Four-year, small, primarily nonresidential', 
                'Four-year, small, primarily residential', 
                'Four-year, small, highly residential', 
                'Four-year, medium, primarily nonresidential', 
                'Four-year, medium, primarily residential', 
                'Four-year, medium, highly residential', 
                'Four-year, large, primarily nonresidential', 
                'Four-year, large, primarily residential', 
                'Four-year, large, highly residential', 
                'Exclusively graduate/professional']
    replace_dict1 = dict(zip(list_values1, text_values1))
    df['CCSIZSET'] = df['CCSIZSET'].replace(replace_dict1)
    return df


def update_school_religion(df):
    '''
    Converts the RELAFFIL column to a plain language string.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df['RELAFFIL'] = df['RELAFFIL'].fillna(-1)
    df['RELAFFIL'] = df['RELAFFIL'].astype(int)
    list_values2 = [-1, -2, 22, 24, 27, 28, 30, 33, 34, 35, 36, 37, 38, 
                39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 
                53, 54, 55, 57, 58, 59, 60, 61, 64, 65, 66, 67, 68, 
                69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 84, 87, 
                88, 89, 91, 92, 93, 94, 95, 97, 99, 100, 101, 102, 
                103, 105, 106, 107]
    text_values2 = ['Not reported', 
                'Not applicable', 
                'American Evangelical Lutheran Church', 
                'African Methodist Episcopal Zion Church', 
                'Assemblies of God Church', 
                'Brethren Church', 
                'Roman Catholic', 
                'Wisconsin Evangelical Lutheran Synod', 
                'Christ and Missionary Alliance Church', 
                'Christian Reformed Church', 
                'Evangelical Congregational Church', 
                'Evangelical Covenant Church of America', 
                'Evangelical Free Church of America', 
                'Evangelical Lutheran Church', 
                'International United Pentecostal Church', 
                'Free Will Baptist Church', 
                'Interdenominational', 
                'Mennonite Brethren Church', 
                'Moravian Church', 
                'North American Baptist', 
                'Pentecostal Holiness Church', 
                'Christian Churches and Churches of Christ', 
                'Reformed Church in America', 
                'Episcopal Church, Reformed', 
                'African Methodist Episcopal', 
                'American Baptist', 
                'American Lutheran', 
                'Baptist', 
                'Christian Methodist Episcopal', 
                'Church of God', 
                'Church of Brethren', 
                'Church of the Nazarene', 
                'Cumberland Presbyterian', 
                'Christian Church (Disciples of Christ)', 
                'Free Methodist', 
                'Friends', 
                'Presbyterian Church (USA)', 
                'Lutheran Church in America', 
                'Lutheran Church - Missouri Synod', 
                'Mennonite Church', 
                'United Methodist', 
                'Protestant Episcopal', 
                'Churches of Christ', 
                'Southern Baptist', 
                'United Church of Christ', 
                'Protestant, not specified', 
                'Multiple Protestant Denomination', 
                'Other Protestant', 
                'Jewish', 
                'Reformed Presbyterian Church', 
                'United Brethren Church', 
                'Missionary Church Inc', 
                'Undenominational', 
                'Wesleyan', 
                'Greek Orthodox', 
                'Russian Orthodox', 
                'Unitarian Universalist', 
                'Latter Day Saints (Mormon Church)', 
                'Seventh Day Adventists', 
                'The Presbyterian Church in America', 
                'Other (none of the above)', 
                'Original Free Will Baptist', 
                'Ecumenical Christian', 
                'Evangelical Christian', 
                'Presbyterian', 
                'General Baptist', 
                'Muslim', 
                'Plymouth Brethren']
    replace_dict2 = dict(zip(list_values2, text_values2))
    df['RELAFFIL'] = df['RELAFFIL'].replace(replace_dict2)
    return df


def impute_missing_values(df):
    '''
    Replaces missing values with the imputed median column values.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = SimpleImputer(strategy='median').fit_transform(df[[column]])
    return df


def update_index(df):
    '''
    Converts the row index to the school names.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df = df.set_index('INSTNM')
    return df


def clean_data(df):
    '''
    Cleans and filters the data so it can be used to calculate the Gower's Distance.
    :param df: pandas dataframe
    :return: pandas dataframe
    '''
    df = drop_nulls(df)
    df = remove_duplicates(df)
    df = merge_columns(df)
    df = fix_multitype_columns(df)
    df = update_school_size(df)
    df = update_school_religion(df)
    df = impute_missing_values(df)
    df = update_index(df)
    return df
