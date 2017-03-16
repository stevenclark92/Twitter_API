#Remove redundant imports, make use of unused ones
import sys
import operator
import requests
import json
import io
import twitter
import pymongo

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

class User(object):
    
    def __init__(self, handle):
        self.handle = handle   
    
    def profile(self):
        self.profile
        user_profile = twitter_api.GetUser(screen_name = self.handle)
        dict_profile = user_profile.AsDict()
        return dict_profile
    
    def tweets(self):
        self.tweets        
        user_tweets = twitter_api.GetUserTimeline(screen_name = self.handle, count = 200, include_rts = False)
        return user_tweets
       
    def followers(self):
        self.followers
        user_followers = twitter_api.GetFollowerIDsPaged(screen_name = self.handle)
        return user_followers

    def following(self):
        self.following
        user_following = twitter_api.GetFriendIDsPaged(screen_name = self.handle)
        return user_following

def unified_profile_builder(account_name):
    account = User(account_name)
    dict_lists = {"Tweets": account.tweets(), "Followers": account.followers(), "Following": account.following()}
    combined_dict = account.profile().copy()
    combined_dict.update(dict_lists)
    return combined_dict

unified_profile_builder("")