#!/usr/bin/env python
# coding: utf-8

# In[25]:


# libs import
import requests, json, response
import pandas as pd
from time import sleep
from datetime import datetime, date
import numpy as np



# In[26]:


# Config of navigation heders requests

head = {
        'x-guest-token':'1559599654475632641',
        'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
}

baseUrl = 'https://twitter.com/i/api/1.1/users/recommendations.json?limit=100'# <-- Config limit of users scraper


req = requests.get(baseUrl, headers=head) # Request https
req = req.text
data = pd.read_json(req)
df1 = pd.DataFrame(data) # Creating dataframe
print(df1)

df1 = df1['user']
df1 = pd.DataFrame(list(df1))

df1 = df1[[  # Select colluns of table
           
            'id',
            'name',
            'screen_name',
            'description',
            'followers_count',
            'friends_count',
            'created_at',
            'location',
            'favourites_count',
            'statuses_count',
            'url'
            
        ]]

df1 = df1[0:51] # Range of scraper

var = df1['id'] 
users_id = []
for i in var:
    users_id.append(i) # Define list id


# In[27]:


class datecalc: # creating class and function of calculate 'day','month','yaer' diference
    
    def day_diff(i):
        
        s = list(df1['created_at'][i].split())
        day = s[2]
        month = s[1]
        year = s[-1]
                
                            # Treating the format of dates perform the calculations
        if month == 'Jan':
            month = month.replace('Jan', '01')
        elif month == 'Feb':
            month = month.replace('Feb','02' )
        elif month == 'Mar':
            month = month.replace('Mar', '03')
        elif month == 'Apr':
            month = month.replace('Apr', '04')
        elif month == 'May':
            month = month.replace('May', '05')
        elif month == 'Jun':
            month = month.replace('Jun', '06')
        elif month == 'Jul':
            month = month.replace('Jul', '07')
        elif month == 'Aug':
            month = month.replace('Aug', '08')
        elif month == 'Sep':
            month = month.replace('Sep', '09')
        elif month == 'Oct':
            month = month.replace('Oct', '10')
        elif month == 'Nov':
            month = month.replace('Nov', '11')
        elif month == 'Dec':
            month = month.replace('Dec', '12')
        
        
        today = str(date.today())
        today = list(today.split('-'))
        monthNow = int(today[1])
        yearNow = int(today[0])
        dayNow = int(today[2])

        day = int(day)
        month = int(month)
        year = int(year)

        old_date = datetime(year,month,day)
        now_date = datetime(yearNow, monthNow, dayNow)
        time_diff = now_date - old_date
        time_diff = str(time_diff).split()
        time_diff = int(time_diff[0])
        return time_diff
        
     # Calculate mean, median  
        
        
    def week_diff(i):
        days = datecalc.day_diff(x)
        week = (days / 7)
        return week
        
    def month_diff(i):
        week = datecalc.week_diff(x)
        month = (week / 4)
        return month
    
    def mean_day(i):
        days = datecalc.day_diff(x)
        mean_day = (days / 2)
        mean_day = round(mean_day, 2)
        return mean_day
    
    def mean_week(i):
        week = datecalc.week_diff(x)
        mean_week = (week / 2)
        mean_week = round(mean_week,2)
        return mean_week
    
    def mean_month(i):
        month = datecalc.month_diff(x)
        mean_month = (month/ 2)
        mean_month = round(mean_month, 2)
        return mean_month
    
    def median_day(i):
        days = datecalc.day_diff(x)
        median_day = df1['statuses_count'][x] / days
        return median_day
    
    def median_week(i):
        week = datecalc.week_diff(x)
        median_week = df1['statuses_count'][x] / week
        return median_week
    
    def median_month(i):
        month = datecalc.month_diff(x)
        median_month = df1['statuses_count'][i] / month
        return median_month
    


# In[28]:


quote = 0 
reply = 0 
retweet = 0
mean_quote = 0
mean_reply = 0
mean_tweet = 0
last_10 = []


# Scraping data from public url allowed by 'Tweet'

for x in range(51):
    if x == 40:
        continue    # delete ruids is here 
    print(x)

    user_id = users_id[x]
    url = f'https://twitter.com/i/api/graphql/X0G3yrqmH2bBryO4kPAVMQ/UserTweets?variables=%7B%22userId%22%3A%22{user_id}%22%2C%22count%22%3A50%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22dont_mention_me_view_api_enabled%22%3Atrue%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_uc_gql_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'
    req = requests.get(url, headers=head)
    req = req.text
    
    # Last 10 tweets from user profile
    for i in range(10, 20):

        data = json.loads(req)
        data = data['data']
        data = data['user']
        data = data['result']
        data = data['timeline_v2']
        data = data['timeline']
        data = data['instructions'][1]
        data = data['entries'][i]
        data = data['content']
        data = data["itemContent"]
        data = data['tweet_results']
        data = data['result']
        df = pd.DataFrame(data)
        df = pd.DataFrame(df['legacy'])
        df = df.T # Reverse dataframe
        df = df.reset_index(drop=True)
        
        
        # Adding quotes within 10 tweets
        quote_count = int(df['quote_count'])
        quote = quote + quote_count
        
        # Adding replys within 10 tweets
        reply_count = int(df['reply_count'])
        reply = reply + reply_count
        
        # Adding retweet within 10 tweets
        retweet_count = int(df['retweet_count'])
        retweet = retweet + retweet_count
     
    # Using the function to calculate the average based on that shaved user profile
    median_day = datecalc.median_day(x)
    median_week = datecalc.median_week(x)
    median_month = datecalc.median_month(x)
    
    # Using the function to calculate the mean based on that shaved user profile
    mean_day = datecalc.mean_day(x)
    mean_week = datecalc.mean_week(x)
    mean_month = datecalc.mean_month(x)
    

    
    print(mean_quote)
    
    # Adding data to a list
    last_10.append([user_id, quote, reply, retweet, median_day, median_week, median_month, mean_day, mean_week, mean_month])
    
    print(last_10)


# In[30]:


df2 = pd.DataFrame(last_10)

# Defining name for shaved columns
df2.rename(columns = {
                        0:'id', 
                        1:'quote',
                        2:'reply',
                        3:'retweet', 
                        4:'medianDay_tweet', 
                        5:'medianWeek_tweet', 
                        6:'medianMonth_tweet',
                        7:'meanDay_tweet',
                        8:'meanWeek_tweet',
                        9:'meanWonth_tweet'}, inplace = True)


df = pd.merge(df1, df2, how = 'inner', on = 'id') # Merge between df1 and df2


df.to_excel('dataset.xlsx') # Exporting analysis report


# In[ ]:




