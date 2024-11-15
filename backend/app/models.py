from app.db import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_screen_name = db.Column(db.String(50), nullable=False)
    user_description = db.Column(db.String(300), nullable=False)
    user_join_date = db.Column(db.TIMESTAMP, nullable=False)
    user_followers_count = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_screen_name': self.user_screen_name,
            'user_description': self.user_description,
            'user_join_date': self.user_join_date,
            'user_followers_count': self.user_followers_count
        }


class Location(db.Model):
    __tablename__ = 'locations'
    lat = db.Column(db.Float, primary_key=True)
    long = db.Column(db.Float, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    continent = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'lat': self.lat,
            'long': self.long,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'continent': self.continent
        }


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

    def to_dict(self):
        return {
            'tweet_id': self.tweet_id,
            'tweet': self.tweet,
            'likes': self.likes,
            'retweet_count': self.retweet_count,
            'source': self.source,
            'created_at': self.created_at.isoformat(),
            'collected_at': self.collected_at.isoformat(),
            'tweet_about': self.tweet_about,
            'user_id': self.user_id,
            'lat': self.lat,
            'long': self.long,
        }
