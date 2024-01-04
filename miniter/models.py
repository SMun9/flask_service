from miniter import db
import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, name='unique_email_constraint')  # Use 'unique=True' for unique constraint
    hashed_password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)  # Fix 'created_at' typo

    def __repr__(self):
        return f"<User {self.name}>"

class UsersFollowList(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE', name='users_follow_list_user_id_fkey'), primary_key=True)
    follow_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE', name='users_follow_list_follow_user_id_fkey'), primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    user = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('followed_users', lazy='dynamic'))
    follow_user = db.relationship('Users', foreign_keys=[follow_user_id], backref=db.backref('followers', lazy='dynamic'))

    def __repr__(self):
        return f"<UsersFollowList {self.user_id} follows {self.follow_user_id}>"

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE', name='tweets_user_id_fkey'), nullable=False)
    tweet = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    user = db.relationship('Users', backref=db.backref('tweets', lazy=True))
    # __table_args__ = ( db.ForeignKeyConstraint(
    #     ["user_id"], ["users.id"], name="tweets_user_id_fkey"
    # ),)
    
    def __repr__(self):
        return f"<Tweet {self.id} by {self.user_id}>"
   
    


