![start with why](https://img.shields.io/pypi/l/tweepy)
![](https://img.shields.io/pypi/l/pandas)
[![Documentation Status](http://img.shields.io/badge/docs-v3.9.0-brightgreen.svg?style=flat)](http://docs.tweepy.org)
[![Version](http://img.shields.io/pypi/v/tweepy.svg?style=flat)](https://pypi.org/project/tweepy/)
[![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)
# Analysing Streaming Tweets with Python and PostgreSQL 
create a small project of analysing streaming Tweets.
From extracting data from the source and storing it into a PostgreSQL database to processing that data and preparing it for analysis tasks, we will try to understand the workflow of a data engineer’s task.
And to bring closure to this project, we will analyse this data towards the end and see if we can come up with some valuable insights.

Tweepy: Twitter for Python
======
###  Installing relevant Libraries
```pip install tweepy```

Or use Git to clone the repository from GitHub.

```git clone https://github.com/tweepy/tweepy.git```

psycopg libraries to access the PostgreSQL database from Python.
You can install psycopg using the pip command.

```pip install psycopg```



### Creating Twitter Developer Account
To stream data from Twitter, you will need to head over to the Twitter developer’s website and register your app to get access to the Twitter APIs. The steps are pretty straightforward. However, you need to provide a good explanation as to what you are going to do with the data you receive from Twitter. Hence, this might take a while, but you should be able to get this done pretty easily.

Once you have registered your app, you will be provided with an API access key and API secret key. Store these keys in a safe place because they will only be generated once and you will need them, again and again, to connect to the API.

![name-of-you-image](https://github.com/dbenshimol/Twitter_API/blob/master/Images/twitter-develop.png)

### PostgreSQL Database
Postgresql is a relational database management system based on SQL. It is free and open-source and works well on all Operating Systems. Further, it has a proven reputation for safely and robustly storing your data and supports both SQL (relational) and JSON(non-relational) based querying.

Postgresql has properties like asynchronous replication, multi-version concurrency control, and many more. Additionally, Postgresql is also highly extensible. You can create your own data types, index types, and more. Besides supporting the primitive data types like boolean, characters, integers, etc., Postgresql also has some additional data types related to geometry like a box, line, polygon, etc.

Postgresql is widely used as a back-end database with many dynamic websites and web applications and provides support for many languages like Python, Java, C++, and more.

![name-of-you-image](https://github.com/dbenshimol/Twitter_API/blob/master/Images/PostgreSQL.png)

### Authenticating the Twitter API
Tweepy supports both OAuth 1a (application-user) and OAuth 2 (application-only) authentication. Authentication is handled by the tweepy.AuthHandler class.
