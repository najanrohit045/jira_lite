from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(300),nullable=False)

    def __repr__(self):
        return f"User {self.username}"
    
class Project(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)

    description=db.Column(db.String(300))

class Issue(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(500))

    status=db.Column(db.String(100),default="todo")

    project_id=db.Column(db.Integer,db.ForeignKey('project.id'))

    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))