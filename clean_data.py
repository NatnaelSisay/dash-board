''' 
This file will clean the data for 
semantic and topic analysis purposes.
'''
import pandas as pd
from add_data import db_execute_fetch




def loadData():
    query = "select * from TweetInformation"
    df = db_execute_fetch(query, dbName="tweets", rdf=True)
    return df

def info():
  number_of_empty_texts = df['clean_text'].isnull().sum()
  shape = df.shape
  return (number_of_empty_texts, shape)

df = loadData()

cleanTweet = pd.DataFrame()
cleanTweet['clean_text'] = df['clean_text']
cleanTweet['polarity'] = df['polarity']