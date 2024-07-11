'''
The file executes the full process of loading school data, cleaning the data, 
running Gower's distance, and creating a dataset of similar colleges.
To run this in the terminal, a user needs to:
- Provide the path to the input csv file
- Provide the path to save the Gower's distance matrix
- Provide the path to save the similar colleges dataset
Example: python main.py SchoolData.csv gower_distance.csv similar_colleges.csv
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
    print("Saving Gower's Distance Matrix")
    save_csv(df_gower, sys.argv[2])
    print("Creating Similar Colleges Dataset")
    df_similar = create_similar_colleges(df_gower)
    print("Saving Similarity Dataset")
    save_csv(df_similar, sys.argv[3])
    print("Done")
