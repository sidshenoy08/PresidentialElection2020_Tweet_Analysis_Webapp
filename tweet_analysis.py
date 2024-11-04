# -*- coding: utf-8 -*-
"""Tweet Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQnM4dL4xpqGMS2XOSTYcmGooFgDENWi
"""

import pandas as pd

"""# **Donald Trump Tweet Dataset**"""

trump_df = pd.read_csv('hashtag_donaldtrump.csv', lineterminator='\n')

"""Attributes in the dataset

*   created_at: Date and time of tweet creation
*   tweet_id: Unique ID of the tweet


*   tweet: Full tweet text
*   likes: Number of likes

*   retweet_count: Number of retweets
*   source: Utility used to post tweet

*   user_id: User ID of tweet creator
*   user_name: Username of tweet creator

*   user_screen_name: Screen name of tweet creator
*   user_description: Description of self by tweet creator

*   user_join_date: Join date of tweet creator
*   user_followers_count: Followers count on tweet creator

*   user_location: Location given on tweet creator's profile
*   lat: Latitude parsed from user_location

*   long: Longitude parsed from user_location
*   city: City parsed from user_location

*   country: Country parsed from user_location
*   state: State parsed from user_location

*   state_code: State code parsed from user_location
*   collected_at: Date and time tweet data was mined from twitter

Decompose into tweets, users, location
"""

print(trump_df.info())

trump_df.head()

trump_df['created_at'].sort_values()

print(trump_df.groupby('country').first().loc[:,('tweet')])

print(trump_df.country.unique())

print(trump_df.continent.unique())

trump_df.isnull().sum(axis=0)

print(trump_df.dtypes)

print("Highest number of likes: {}".format(trump_df['likes'].max()))
print("Highest number of retweets: {}".format(trump_df['retweet_count'].max()))
print("Highest number of user followers: {}".format(trump_df['user_followers_count'].max()))

print("For likes, Mean: {0:.3f} ".format(trump_df['likes'].mean()))

trump_df.describe()

trump_df['user_id'].nunique()

print(trump_df.groupby('user_id').first().loc[:, ('user_name', 'user_followers_count')].sort_values(by='user_followers_count', ascending=False))

print(trump_df.groupby('country')['tweet_id'].count().sort_values(ascending=False))

trump_df.dropna(inplace=True)

trump_df.info()

trump_df.isnull().sum(axis=0)

print(trump_df.continent.unique())

print(trump_df.groupby('country')['tweet_id'].count().sort_values(ascending=False))

print(trump_df.groupby('country')['retweet_count'].sum().sort_values(ascending=False))

print(trump_df.groupby('user_name')['tweet_id'].count().sort_values(ascending=False))

print(trump_df.city.unique())

print(trump_df.loc[trump_df['country'] == 'India', 'state' ].unique())

print(trump_df.loc[trump_df['country'] == 'United States of America', 'city' ].unique())

print("For user_followers_count, Mean: {0}, Standard Deviation: {1}, Min: {2}, Max: {3}".format(trump_df['user_followers_count'].mean(), trump_df['user_followers_count'].std(), trump_df['user_followers_count'].min(), trump_df['user_followers_count'].max()))

trump_df.head()

trump_users_df = trump_df[['user_id', 'user_name', 'user_screen_name', 'user_description', 'user_join_date', 'user_followers_count']]

trump_users_df.head()

trump_users_df.info()

trump_users_df[trump_users_df.duplicated()]

trump_users_df['user_id'].nunique()

trump_locations_df = trump_df[['lat', 'long', 'city', 'state', 'state_code', 'country', 'continent']]

trump_locations_df.head()

trump_locations_df.info()

# drop state_code as it has no practical use
trump_locations_df.drop(['state_code'], axis=1, inplace=True)

trump_locations_df[['lat', 'long']].nunique()

trump_tweets_df = trump_df[['tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'created_at', 'collected_at', 'user_id', 'user_location', 'lat', 'long']]

trump_tweets_df.loc[:, "tweet_about"] = "Trump"

# drop user_location as lat and long are parsed from this field
trump_tweets_df.drop(['user_location'], axis=1, inplace=True)

trump_tweets_df = trump_tweets_df[['tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'created_at', 'collected_at', 'tweet_about', 'user_id', 'lat', 'long']]

trump_tweets_df.head()

trump_tweets_df['tweet_about'].unique()

trump_tweets_df.info()

trump_tweets_df['tweet_id'].nunique()

"""# **Joe Biden Tweet Dataset**"""

biden_df = pd.read_csv('hashtag_joebiden.csv',lineterminator='\n')

biden_df.info()

biden_df.describe()

print("For user_followers_count, Mean: {0}, Standard Deviation: {1}, Min: {2}, Max: {3}".format(biden_df['user_followers_count'].mean(), biden_df['user_followers_count'].std(), biden_df['user_followers_count'].min(), biden_df['user_followers_count'].max()))

biden_df.dropna(inplace=True)

biden_df.info()

biden_df.isnull().sum(axis=0)

biden_users_df = biden_df[['user_id', 'user_name', 'user_screen_name', 'user_description', 'user_join_date', 'user_followers_count']]

biden_users_df.info()

biden_users_df[biden_users_df.duplicated()]

biden_users_df.info()

biden_users_df['user_id'].nunique()

biden_locations_df = biden_df[['lat', 'long', 'city', 'state', 'state_code', 'country', 'continent']]

biden_locations_df.info()

# drop state_code as it has no practical use
biden_locations_df.drop(['state_code'], axis=1, inplace=True)

biden_locations_df[['lat', 'long']].nunique()

biden_tweets_df = biden_df[['tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'created_at', 'collected_at', 'user_id', 'user_location', 'lat', 'long']]

# drop user_location as lat and long are parsed from this field
biden_tweets_df.drop(['user_location'], axis=1, inplace=True)

biden_tweets_df.loc[:, "tweet_about"] = "Biden"

biden_tweets_df = biden_tweets_df[['tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'created_at', 'collected_at', 'tweet_about', 'user_id', 'lat', 'long']]

biden_tweets_df.head()

biden_tweets_df['tweet_about'].unique()

biden_tweets_df['tweet_id'].nunique()

"""# **Combining the datasets**"""

trump_tweets_df['tweet_id'].nunique() + biden_tweets_df['tweet_id'].nunique()

tweets_df = pd.concat([trump_tweets_df, biden_tweets_df])

tweets_df.info()

tweets_df.head()

tweets_df.tail()

# shuffle the merged dataframe
tweets_df = tweets_df.sample(frac=1)

tweets_df.head()

# convert ids to integer notation
tweets_df[['tweet_id', 'likes', 'retweet_count', 'user_id']] = tweets_df[['tweet_id', 'likes', 'retweet_count', 'user_id']].astype(int)

tweets_df.head()

tweets_df['tweet_id'].nunique()

# drop rows having duplicate tweet_ids to enforce Primary Key constraint in tweets relation
tweets_df.drop_duplicates(subset=['tweet_id'], inplace=True)

print(tweets_df['tweet_id'].max())
print(tweets_df['user_id'].max())
print(tweets_df['tweet'].str.len().max())

tweets_df['source'].str.len().max()

tweets_df.info()

users_df = pd.concat([trump_users_df, biden_users_df])

users_df.info()

users_df['user_id'].nunique()

# drop rows having duplicate user_ids to enforce Primary Key constraint in tweets relation
users_df.drop_duplicates(subset=['user_id'], inplace=True)

users_df.info()

users_df.head()

users_df[['user_id', 'user_followers_count']] = users_df[['user_id', 'user_followers_count']].astype(int)

print(users_df['user_name'].str.len().max())
print(users_df['user_screen_name'].str.len().max())
print(users_df['user_description'].str.len().max())

users_df.head()

locations_df = pd.concat([trump_locations_df, biden_locations_df])

locations_df.info()

locations_df[['lat', 'long']].nunique()

# drop rows having duplicate (lat, long) to enforce Primary Key constraint in tweets relation
locations_df.drop_duplicates(subset=['lat', 'long'], inplace=True)

print(locations_df['city'].str.len().max())
print(locations_df['state'].str.len().max())
print(locations_df['country'].str.len().max())
print(locations_df['continent'].str.len().max())

locations_df.info()

locations_df.head()



"""# **Final Relations**"""

tweets_df.info()

tweets_df.head()

users_df.info()

users_df.head()

locations_df.info()

locations_df.head()



"""# **Exporting the relations**"""

tweets_df.to_csv('tweets.csv', index=False)

users_df.to_csv('users.csv', index=False)

locations_df.to_csv('locations.csv', index=False)

