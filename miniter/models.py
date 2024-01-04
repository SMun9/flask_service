from miniter import db
import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(2000), nullable=False)
    create_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    
    # Unique constraint on the email column in the User table
    db.UniqueConstraint('email', name='unique_email_constraint')
    

class UsersFollowList(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    follow_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    create_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    # user = db.relationship('Users', backref=db.backref('UsersFollowList', lazy=True))
    db.ForeignKeyConstraint(
        ["user_id", "follow_user_id"], ["users.id", "users.id"], \
        name=["users_follow_list_user_id_fkey", "users_follow_list_follow_user_id_fkey"]
    ),
    

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    tweet = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    users = db.relationship("Users", backref=db.backref("user_set"))
    db.ForeignKeyConstraint(
        ["user_id"], ["users.id"], name="tweets_user_id_fkey"
    ),
    


