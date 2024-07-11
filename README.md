# University Similarity by Gower's Distance
An exploration of universities by [Gower's Distance](https://en.wikipedia.org/wiki/Gower%27s_distance), which accounts for categorical, binary, and numeric data types. 

If a student has a future univerity in mind, this would help them find other, similar schools to consider. The end result is that a user can input a school name and the script returns the top ten similar schools and Gower's distance measures. 

The additional intent is that this script can be used in future years when new data is published, assuming the similar format that has been used in numerous previous years. 

The steps involved include:
1. Loading data from a .csv file
2. Cleaning data
3. Visually exploring the distribution of some of the features
4. Calculating the Gower's distances between schools
5. Creating an executing a function to identify schools similar to an input school

### Data
This uses datafrom the U.S. Department of Education College Scorecard. 

Data can be downloaded [here](https://collegescorecard.ed.gov/data/), and the documentation is available [here](https://collegescorecard.ed.gov/data/documentation/). 

A note that the original dataset is just over 100MB. GitHub does not like files of this size, so the repository has a reduced dataset (with less columns but all the schools). The original notebook contains the step on which columns were retained from the original dataset. 

### Environment & Packages
Specifics are included in the requirements.txt file. 

### Outputs
1. A Gower's Matrix of similarity results, as a csv, that can be used for further data science modeling. 

2. A csv that contains the input school and the top ten most similar schools. Like below:

| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|input_school|similar1|similar2|similar3|similar4|similar5|similar6|similar7|similar8|similar9|similar10|
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
University of Michigan-Ann Arbor | University of Maryland-College Park | University of Florida | University of Illinois Urbana-Champaign | University of Southern California | University of Virginia-Main Campus | Northwestern University | Rutgers University-New Brunswick | University of Wisconsin-Madison | New York University | Cornell University |
