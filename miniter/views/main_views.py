from flask import Blueprint, jsonify, request
from miniter import db
from miniter.models import Users, Tweets

bp = Blueprint("main", __name__, url_prefix='/')


@bp.route('/')
def index():
    return "Miniter index"

@bp.route("/hello")
def hello_miniter():
    return "Hello, Miniter!"


@bp.route("/ping", methods=["GET"])
def ping():
    return "pong"

@bp.route("/sign-up", methods=["POST"])
def sign_up():
    new_user = request.json
    user_data  = Users(name=new_user["name"],
                  email=new_user["email"],
                  hashed_password=new_user["password"],
                  profile=new_user["profile"])
    
    db.session.add(user_data)
    db.session.commit()
    
    created_user = {
        "id" : user_data.id,
        "name": user_data.name,
        "email": user_data.email,
        "profile": user_data.profile,
    } if user_data else None
    
    return jsonify(created_user)
    
@bp.route("/tweet", methods=["POST"])
def tweet():
    user_tweet = request.json
    user_id = user_tweet["id"]
    tweet = user_tweet["tweet"]
    user = Users.query.get(user_id)
    
    if not user:
        return "User not found.", 404
    
    if len(tweet) > 300:
        return "tweet이 300자를 초과했습니다", 400
    
    tweet_data = Tweets(user_id=user_tweet["id"], tweet=tweet)
    db.session.add(tweet_data)
    db.session.commit()
    
    return '', 200
    

