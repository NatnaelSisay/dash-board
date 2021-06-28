import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px

import clean_data

def text_category(polarity):
    if (polarity > 0):
        return 'positive'
    elif (polarity < 0):
        return 'negative'
    else:
        return 'neutral' 


def run():
  st.write('# Sentiment Analysis')
  st.write('## Check Clean Tweet Head')
  st.write(clean_data.cleanTweet.head())
  
  # New Column 
  clean_data.cleanTweet['score'] = clean_data.cleanTweet['polarity'].apply(text_category)
  clean_data.cleanTweet['score'].value_counts()

  # bar chart
  score_count = clean_data.cleanTweet['score'].value_counts()
  st.write('## Polarty of datas')
  st.bar_chart(score_count)

  class Sentimet:
    def __init__(self, cleanTweet):
        self.tweats_list = cleanTweet

    def run(self):
        print(self.tweats_list)


