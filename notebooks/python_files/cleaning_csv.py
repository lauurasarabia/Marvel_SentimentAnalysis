import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

def reading_csv(file):
    """ Reading csv files as a DataFrame with pandas"""
    df = pd.read_csv(f"/Users/lauurasarabia/Ironhack/projects/project4/data/{file}.csv")
    return df

def dropping_columns():
    """Drop unnecessary columns from marvel df"""
    marvel.drop(['Adam McKay', 'Anna Boden', 
                 'Art Marcum', 'Ashley Edward Miller',
                 'Chris McKenna', 'Christopher Ford', 
                 'Christopher Markus', 'Christopher Yost', 
                 'Craig Kyle', 'Don Payne', 
                 'Drew Pearce', 'Edgar Wright', 
                 'Eric Pearson', 'Erik Sommers',
                 'Geneva Robertson-Dworet', 'Hawk Ostby', 
                 'James Gunn', 'Joe Cornish',
                 'Joe Robert Cole', 'John Francis Daley', 
                 'Jon Watts', 'Jonathan Goldstein', 
                 'Joss Whedon', 'Justin Theroux', 
                 'Mark Fergus', 'Matt Holloway', 
                 'Paul Rudd', 'Ryan Coogler', 
                 'Ryan Fleck', 'Shane Black', 
                 'Stephen McFeely', 'Zack Stentz'
                 ], axis=1, inplace=True)
    return marvel

def drop_rename():
    marvel_sentiment.drop(["Unnamed: 0"], axis=1, inplace=True)
    marvel_sentiment.rename(columns={'character':'full_name'}, inplace=True)
    return marvel_sentiment

def plotting_nltk():
    """Create three different plots for being able to visualize the sentiment analysis (positive, neutral and negative)"""
    fig, axs = plt.subplots(1, 3, figsize=(16,4))
    sns.barplot(data=marvel_sentiment, x='year', y='pos', ax=axs[0])
    sns.barplot(data=marvel_sentiment, x='year', y='neu', ax=axs[1])
    sns.barplot(data=marvel_sentiment, x='year', y='neg', ax=axs[2])
    axs[0].set_title('Positive')
    axs[1].set_title('Neutral')
    axs[2].set_title('Negative')
    plt.tight_layout()
    return plt.show()

def replacing_characters():
    """Change manually character names and removing the spaces at the beginning of character's name for matching both DataFrames"""
    top_characters["character"].replace({' IRON MAN':'TONY STARK',
                                     ' CAPTAIN AMERICA':'STEVE ROGERS',
                                     ' SPIDER MAN':'PETER PARKER',
                                     ' THE INCREDIBLE HULK':'BRUCE BANNER',
                                     ' BLACK WIDOW':'NATASHA ROMANOFF',
                                     ' ANT MAN':'SCOTT LANG',
                                     ' HAWKEYE':'CLINT BARTON',
                                     ' BLACK PANTHER':"T'CHALLA",
                                     ' FALCON':'SAM WILSON',
                                     ' WAR MACHINE':'JAMES RHODES',
                                     ' THE WINTER SOLDIER':'BUCKY BARNES',
                                     ' DR STRANGE':'STEPHEN STRANGE',
                                     ' M BAKU':"M'BAKU",
                                    }, inplace=True)
    top_characters["character"] = top_characters.character.str.lstrip().str.lstrip('_')
    return top_characters

def cleaning_df():
    """Drop unnecessary columns and replacing special characters for underscores"""
    movie_top_characters.drop(['Unnamed: 0', '0'], axis=1, inplace=True)
    movie_top_characters.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)
    movie_top_characters.rename(columns=lambda x: x.strip().replace(":", ""), inplace=True)
    movie_top_characters.rename({"character":"full_name"}, axis=1, inplace=True)
    return movie_top_characters

