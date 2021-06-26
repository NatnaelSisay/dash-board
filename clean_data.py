''' 
This file will clean the data for 
semantic and topic analysis purposes.
'''
import pandas as pd
from day5 import loadData

df = loadData()

cleanTweet = pd.DataFrame()
cleanTweet['clean_text'] = df['clean_text']
cleanTweet['polarity'] = df['polarity']


def info():
  number_of_empty_texts = df['clean_text'].isnull().sum()
  shape = df.shape
  return (number_of_empty_texts, shape)

