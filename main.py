'''
The file executes the data cleaning process and loads the data from csv files.
'''

import sys
from test import all_tests
from loaders import load_data
from data_cleaning import clean_data
from gowers import similarity_matrix
from similarschools import create_similar_colleges
from savers import save_csv


if __name__ == '__main__':
    print("Loading Data")
    data = load_data(sys.argv[1])
    print("Cleaning Data")
    data = clean_data(data)
    print("Testing Data")
    all_tests(data)
    print("Running Gower's Distance")
    df_gower = similarity_matrix(data)
    print("Creating Similar Colleges Dataset")
    df_similar = create_similar_colleges(df_gower)
    print("Saving New Dataset")
    save_csv(df_similar, sys.argv[2])
    print("Done")
