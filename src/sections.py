from flask import Blueprint, request, jsonify, Response
from src.database import Section, Item, Modifiers, db

sections = Blueprint("sections", __name__, url_prefix="/api/v1/sections")

@sections.get('/')
def getSections():
    section = Section.query.all()
    data = []

    for sec in section:
        data.append({
            'id': sec.id,
            'name': sec.name,
            'description': sec.description
        })

    return jsonify({
        'data': data
    }), 200


@sections.get('/<int:id>')
def getSection(id):
    section = Section.query.filter_by(id=id)
    data = []

    for sec in section:
        data.append({
            'id': sec.id,
            'name': sec.name,
            'description': sec.description
        })
    
    return jsonify({
        'data': data
    }), 200

    


@sections.post('/')
def createSection():
    name = request.json.get('name', '')
    description = request.json.get('description', '')

    section = Section(name=name, description=description)
    db.session.add(section)
    db.session.commit()

    return jsonify({
        'id': section.id,
        'name': section.name,
        'description': section.description
    }), 201


@sections.put('/<int:id>')
def updateSection(id):
    section_to_update = Section.query.filter_by(id=id).first()
    if section_to_update:
        section_to_update.name = request.json.get('name', '')
        section_to_update.description = request.json.get('description', '')
        db.session.commit()
        response = Response("Section Updated", status=200, mimetype='application/json')
    else:
        response = Response("Section Not Found", status=404, mimetype='application/json')
    
    return response


@sections.delete('/<int:id>')
def deleteSection(id):
    Section.query.filter_by(id=id).delete()
    db.session.commit()
    response = Response("Section Deleted", status=200, mimetype='application/json')

    return response

