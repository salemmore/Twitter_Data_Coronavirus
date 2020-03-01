import tweepy
import pandas
import numpy as np
from sklearn import datasets
import csv
from collections import Counter
import ast
import codecs
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Access tokens
access_key = 'place_key_here'
access_secret = 'place_token_here'
consumer_key = 'place_key_here'
consumer_secret = 'place_token_here'

# Twitter allows access to only 3240 tweets via this method

# Authorization and initialization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "coronavirus"  # + " -filter:retweets"
date_since = "2019-12-01" #YYYY-MM-DD

# Collect tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5000)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets] #think this is enough to get my heatmap but I really need geocoordinates
users_locs

tweet_text = pandas.DataFrame(data=users_locs, 
                     columns=['user', "location"])  #this saved my life. didn't know how to turn twitter search query into dataframe
tweet_text

df = pd.DataFrame(tweet_text)


tweets = df

#Converting the location to geocoordinates to be able to plot on a map

geolocator = Nominatim(user_agent="specify_your_app_name_here")

# Go through all tweets and add locations to 'coordinates' dictionary
coordinates = {'latitude': [], 'longitude': []}
for count, user_loc in enumerate(tweets.location):
    try:
        location = geolocator.geocode(user_loc)
        
        # If coordinates are found for location
        if location:
            coordinates['latitude'].append(location.latitude)
            coordinates['longitude'].append(location.longitude)
            
    # If too many connection requests
    except:
        pass
    
# Instantiate and center a GoogleMapPlotter object to show our map
gmap = gmplot.GoogleMapPlotter(30, 0, 3, apikey="") 

# Insert points on the map passing a list of latitudes and longitudes
gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)

# Save the map to html file
gmap.draw("twitter_data_heatmap.html")
