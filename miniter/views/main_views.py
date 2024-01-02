from flask import Blueprint, jsonify, request

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
    new_user["id"] = id_count
    id_count = id_count + 1
    
    return jsonify(new_user)
    
    

