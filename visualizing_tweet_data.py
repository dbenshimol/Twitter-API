import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tweepy_streamer import TwitterClient, TweetAnalyzer

twitter_client = TwitterClient()
tweet_analyzer = TweetAnalyzer()
api = twitter_client.get_twitter_client_api()

# Analysing user_name : @code
tweets = api.user_timeline(screen_name="code", count=200)
df = tweet_analyzer.tweets_to_data_frame(tweets)


def visualizing_tweet_data(tweets):

    # Get Avg Length of all tweets
    print(np.mean(df['len']))

    # Get the number of likes for the most liked tweet
    print(np.max(df['likes']))

    # Get the number of retweets for the most retweeted tweet
    print(np.max(df['retweets']))

    # Time Series
    # time_likes = pd.Series(data=df['likes'].values, index=df['date'])
    # time_likes.plot(figsize=(16, 4), color='r')
    # plt.show()
    # time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
    # time_retweets.plot(figsize=(16, 4), color='r')
    # plt.show()

    # Layered Time Series:
    time_likes = pd.Series(data=df['likes'].values, index=df['date'])
    time_likes.plot(figsize=(16, 4), label="likes", legend=True)

    time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
    time_retweets.plot(figsize=(16, 4), label="retweets", legend=True)
    plt.show()


visualizing_tweet_data(df)
