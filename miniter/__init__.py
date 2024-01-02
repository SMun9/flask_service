from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.new_user = {}
    app.id_count = 1
    
    # ORM 
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    
    return app
