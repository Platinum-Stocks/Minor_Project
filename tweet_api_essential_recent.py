# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 13:57:11 2022

@author: waseem
"""
#promoter holdings and number holding change parameters to get list 
import pandas as pd
import requests
import os



df = pd.read_excel('list.xlsx', sheetname=0) # can also index sheet by name or fetch all sheets
words = df['Companies'].tolist()
#words= ["Nifty", "NSE", "BSE", "SENSEX", "HDFC", "reliance"]
all_tweet={}
#statuses=[]
b_t = os.environ.get('Bearer_Token')
for word in words:
  #  params = {'q': word,
 #         'lang': 'en',
  #        'count': '100'}
    j=requests.get(
            'https://api.twitter.com/2/tweets/search/recent?query='+word,
            #params=params,
            headers={'authorization': 'Bearer '+ b_t})
    #statuses.append(j)



def get_data(tweet):
    data = {
        'id': tweet['id'],
        'text': tweet['text']
    }
    return data

df = pd.DataFrame()
for tweet in j.json()['data']:
    row = get_data(tweet)
    df = df.append(row, ignore_index=True)
    
