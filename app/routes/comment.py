from flask import Blueprint,request,jsonify

from app import db
from app.models.models import Comment

from app.utils.decorators import login_required

from  flask_jwt_extended import get_jwt_identity

comment_bp=Blueprint('comment',__name__)

@comment_bp.route('/issue/<int:issue_id>/comment',method=['POST'])
@login_required
def create_comment(issue_id):
    data=request.get_json()

    user_id=get_jwt_identity()

    comment=Comment(text=data['text'],issue_id=issue_id)

    db.session.add(comment)
    db.session.commit()

    return jsonify({"message": "Comment added"})

@comment_bp.route('/issues/<int:issue_id>/comments', methods=['GET'])
@login_required
def get_comments(issue_id):
    comments = Comment.query.filter_by(issue_id=issue_id).all()

    result = []
    for c in comments:
        result.append({
            "id": c.id,
            "text": c.text,
            "created_at": c.created_at
        })

    return jsonify(result)