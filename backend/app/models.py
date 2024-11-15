from app.db import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_screen_name = db.Column(db.String(50), nullable=False)
    user_description = db.Column(db.String(300), nullable=False)
    user_join_date = db.Column(db.TIMESTAMP, nullable=False)
    user_followers_count = db.Column(db.Integer, nullable=False)

class Location(db.Model):
    __tablename__ = 'locations'
    lat = db.Column(db.Float, primary_key=True)
    long = db.Column(db.Float, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    continent = db.Column(db.String(20), nullable=False)

class Tweet(db.Model):
    __tablename__ = 'tweets'
    tweet_id = db.Column(db.BigInteger, primary_key=True)
    tweet = db.Column(db.String(1000), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    retweet_count = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    collected_at = db.Column(db.TIMESTAMP, nullable=False)
    tweet_about = db.Column(db.String(5), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.user_id'), nullable=False)
    lat = db.Column(db.Float, db.ForeignKey('locations.lat'), nullable=False)
    long = db.Column(db.Float, db.ForeignKey('locations.long'), nullable=False)
    user = db.relationship('User', backref='tweets')
    location = db.relationship('Location', primaryjoin="and_(Tweet.lat == Location.lat, Tweet.long == Location.long)")