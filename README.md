# University Similarity by Gower's Distance
An exploration of universities by [Gower's Distance](https://en.wikipedia.org/wiki/Gower%27s_distance), which accounts for categorical, binary, and numeric data types. 

If a student has a future univerity in mind, this would help them find other, similar schools to consider. The end result is that a user can input a school name and the script returns the top ten similar schools and Gower's distance measures. 

The additional intent is that this script can be used in future years when new data is published, assuming the similar format that has been used in numerous previous years. 

The steps involved include:
1. Loading data from a .csv file
2. Cleaning data
3. Running some manual checks to confirm value distributions and data types
4. Calculating the Gower's distances between schools, saving the matrix to a .csv
5. Identifying the top 10 most similar schools to the input school, saving the output as a .csv

### Data
This uses datafrom the U.S. Department of Education College Scorecard. 

Data can be downloaded [here](https://collegescorecard.ed.gov/data/), and the documentation is available [here](https://collegescorecard.ed.gov/data/documentation/). 

_A note that the original dataset is just over 100MB. GitHub does not like files of this size, so the repository has a reduced dataset (with less columns but all the schools) saved in the data folder. The original jupyter notebook contains the step on which columns were retained from the original dataset._

### Environment & Packages
Specifics are included in the requirements.txt file. 

### Outputs
1. A Gower's Matrix of similarity results, as a csv, that can be used for further data science modeling. 

2. A csv that contains the input school and the top ten most similar schools. Like below:

|input_school|similar1|similar2|similar3|similar4|similar5|similar6|similar7|similar8|similar9|similar10|
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| University of Michigan-Ann Arbor | University of Maryland-College Park | University of Florida | University of Illinois Urbana-Champaign | University of Southern California | University of Virginia-Main Campus | Northwestern University | Rutgers University-New Brunswick | University of Wisconsin-Madison | New York University | Cornell University |
| The University of Alabama | The University of Tennessee-Knoxville | University of South Carolina-Columbia | Louisiana State University and Agricultural & Mechanical College | University of Arkansas | Michigan State University | University of Delaware | University of Cincinnati-Main Campus | University of Colorado Boulder | University of Oklahoma-Norman Campus | Indiana University-Bloomington | 

### How to Use
Given an environment with Python already installed and in the repository directory, a user should be able to run the following in the terminal: 
```
pip install -r requirements.txt
```

Then:

```
python main.py data/SchoolData.csv data/gower_distance.csv data/similar_colleges.csv
```