from flask import Blueprint,request,jsonify
from app import db
from app.models.models import Issue
from app.utils.decorators import login_required

issue_bp=Blueprint('issue',__name__)

@issue_bp.route('/issue',methods=['POST'])
@login_required
def create_issue():
    data=request.get_json()

    issue=Issue(title=data['title'],description=data.get('description'),project_id=data['project_id'])

    db.session.add(issue)
    db.session.commit()

    return jsonify({"message":"Issue created successfully"})

@issue_bp.route('/issues/<int:issue_id>/assign',methods=['PUT'])
@login_required
def assign_issue(issue_id):

    data = request.get_json()

    issue=Issue.query.get(issue_id)

    if not issue:
        return jsonify({"message":"issue i sn ot found"}), 404
    
    if 'user_id' not in data:
        return jsonify({"message": "user_id is required"}), 400
    
    issue.assigned_to=data['user_id']
    db.session.commit()

    return jsonify({"message":"issue assign successfully"}),200

@issue_bp.route("/issues/<int:issue_id>/update",methods=['POST'])
@login_required
def update_status(issue_id):
    data=request.get_json()
    issue=Issue.query.get(issue_id)
    if not issue:
        return jsonify({"message":"issue not found"}) ,400
    
    issue.status=data['status']

    db.session.commit()

    return jsonify({"message":"update successfully "}) ,200

@issue_bp.route('/issues',methods=['GET'])
@login_required
def get_issue():
    data=request.get_json()

    result=[]

    isssue=Issue.query.all()

    for i in isssue:
        result.append({
            "id":i.id,
            "title":i.title,
            "status":i.status,
            "project_id":i.project_id,
            "assigned_to":i.assigned_to
         })
    return jsonify(result) , 200
        


