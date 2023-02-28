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

def connection_sql (password_sql, dbName):
    connectionData = f"mysql+pymysql://root:{password_sql}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine

