from flask import Blueprint,request,jsonify

from app import db
from app.models.models import Project

from app.utils.decorators import login_required

from flask_jwt_extended import get_jwt_identity

project_bp=Blueprint('project',__name__)

@project_bp.route('/projects',methods=['POST'])
@login_required
def create_project():
    data=request.get_json()

    user_id=get_jwt_identity()
    project=Project(name=data['name'],description=data.get('description'))

    db.session.add(project)
    db.session.commit()

    return jsonify({"message": "Project created successfully"})

@project_bp.route('/projects', methods=['GET'])
@login_required
def get_project():
    projects=Project.query.all()

    result=[]

    for p in projects:
        result.append({"id":p.id,"name":p.name,"description":p.description})

    return jsonify(result)

@project_bp.route('/projects/<int:project_id>', methods=['PUT'])
@login_required
def update_project(project_id):
    data = request.get_json()

    project = Project.query.get(project_id)

    if not project:
        return jsonify({"message": "Project not found"}), 404

    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)

    db.session.commit()

    return jsonify({"message": "Project updated successfully"})

@project_bp.route('/projects/<int:project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    project = Project.query.get(project_id)

    if not project:
        return jsonify({"message": "Project not found"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted successfully"})
