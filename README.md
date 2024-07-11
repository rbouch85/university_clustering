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

