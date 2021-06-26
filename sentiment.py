import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px

from clean_data import cleanTweet

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
  st.write(cleanTweet.head())

  # New Column 
  cleanTweet['score'] = cleanTweet['polarity'].apply(text_category)
  cleanTweet['score'].value_counts()

  # bar chart
  score_count = cleanTweet['score'].value_counts()
  st.write('## Polarty of datas')
  st.bar_chart(score_count)

