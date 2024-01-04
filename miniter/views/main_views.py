from flask import Blueprint, jsonify, request
from miniter import db
from miniter.models import Users

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
    user  = Users(name=new_user["name"],
                  email=new_user["email"],
                  hashed_password=new_user["password"],
                  profile=new_user["profile"])
    
    db.session.add(user)
    db.session.commit()
    
    created_user = {
        "id" : user.id,
        "name": user.name,
        "email": user.email,
        "profile": user.profile,
    } if user else None
    
    return jsonify(created_user)
    
    

