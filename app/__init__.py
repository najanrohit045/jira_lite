from flask import Flask     
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Rohit%40321@localhost/jira_db'
    app.config['JWT_SECRET_KEY'] = 'my-super-secret-key-1234567890-secure'

    db.init_app(app)
    jwt.init_app(app)

    # ✅ MOVE IMPORT HERE
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.project import project_bp
    from app.routes.issue import issue_bp


    app.register_blueprint(project_bp)
    app.register_blueprint(issue_bp)

    return app