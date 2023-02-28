# Project lV - SQL | Tableau



## Marvel Sentiment Analysis
The goal for this project is finding data that is mainly text based in order to clean and transform the data, load it into SQL (through Python), do queries and subqueries (if possible) and generate Tableau visualizations.

The project is divided in four different directories: 
* ***Notebooks*** -> Jupyter Notebooks
* ***Data*** -> CSV files
* ***Python_functions*** -> Executable Python files
* ***Queries*** -> CSV files extracted by SQL queries

### 1. Obtaining data
On the one hand, I downloaded data of Marvel movies and characters. 
I used two different CSV files for the analysis:
- ***mcu.csv*** was used for the sentiment analysis.
- ***characters.csv*** was used for the detail per character in terms of avg lines per movie, avg words, total words, etc.

Moreover, I did some scraping with Selenium to find the 50 main characters and work just with them and not the whole dataset.  

### 2. Cleaning data
After importing both csv files into pandas, I used some functions for cleaning and transforming the data so as to be able to use the SentimentIntensityAnalyzer from nltk library later on. 

### 3. NLTK
Thanks to nltk library I could analyze every line of each movie that I have in my database through an automated process of tagging data according to their sentiment, such as positive, neutral and negative. 
I created a dataframe with this information and merged it with the original data.

![nltk](https://github.com/lauurasarabia/project4/blob/main/images/nltk.png?raw=true)

### 4. SQL Queries
On the other hand, I created a new database in mySQL and exported all the obtained information into it. Using Python, I did some queries to get more detailed information for my visualizations.

### 5.  Tableau
I created the following visualizations in Tableau:

*** In this dashboard we can see the total number of words per character and the year of release per each movie. ***

![dashboard1](https://github.com/lauurasarabia/project4/blob/main/images/movies_characters.png?raw=true)

*** In the first visualization on the dashboard below, you can see how the average compound had its peak on 2010 and kept with ups and downs during the years. The highest point belongs to "Iron Man 2" which is reflected on the second visualization. ***

![dashboard2](https://github.com/lauurasarabia/project4/blob/main/images/compound.png?raw=true)

