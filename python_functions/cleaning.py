import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk

def reading_csv():
    movie_lines = pd.read_csv("/Users/lauurasarabia/Ironhack/projects/project4/data/characters.csv")
    return movie_lines

