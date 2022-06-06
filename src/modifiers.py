from flask import Blueprint, request, jsonify, Response
from src.database import Section, Item, Modifiers, db

modifiers = Blueprint("modifiers", __name__, url_prefix="/api/v1/modifiers")


@modifiers.get('/')
def getModifiers():
    modifiers = Modifiers.query.all()
    data = []

    for mod in modifiers:
        data.append({
            'id': mod.id,
            'description': mod.description,
        })

    return jsonify({
        'data': data
    }), 200


@modifiers.get('/<int:id>')
def getModifier(id):
    modifier = Modifiers.query.filter_by(id=id).first()
    data = []

    data.append({
        'id': modifier.id,
        'description': modifier.description
    })
    
    return jsonify({
        'data': data
    }), 200

    

@modifiers.post('/')
def createModifier():
    description = request.json.get('description', '')

    modifier = Modifiers(description=description)
    db.session.add(modifier)
    db.session.commit()

    return jsonify({
        'id': modifier.id,
        'description': modifier.description
    }), 201


@modifiers.put('/<int:id>')
def updateModifier(id):
    modifier_to_update = Modifiers.query.filter_by(id=id).first()
    if modifier_to_update:
        modifier_to_update.description = request.json.get('description', '')
        db.session.commit()
        response = Response("Modifier Updated", status=200, mimetype='application/json')
    else:
        response = Response("Modifier Not Found", status=404, mimetype='application/json')
    
    return response


@modifiers.delete('/<int:id>')
def deleteModifier(id):
    Modifiers.query.filter_by(id=id).delete()
    db.session.commit()
    response = Response("Modifier Deleted", status=200, mimetype='application/json')

    return response