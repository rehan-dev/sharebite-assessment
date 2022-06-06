from flask import Flask
import os
from src.sections import sections
from src.items import items
from src.modifiers import modifiers
from src.map import mapper
from src.restaurantmenu import restaurantmenu
from src.database import db


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    else:
        app.config.from_mapping(test_config)
    
    db.app=app
    db.init_app(app)

    # JWTManager(app)
    app.register_blueprint(sections)
    app.register_blueprint(items)
    app.register_blueprint(modifiers)
    app.register_blueprint(mapper)
    app.register_blueprint(restaurantmenu)
    # app.register_blueprint(bookmarks)

    with app.app_context():
        db.create_all()
    
    return app