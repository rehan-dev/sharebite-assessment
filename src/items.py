from flask import Blueprint, request, jsonify, Response
from src.database import Section, Item, Modifiers, db

items = Blueprint("items", __name__, url_prefix="/api/v1/items")

@items.get('/')
def getItems():
    items = Item.query.all()
    data = []

    for item in items:
        data.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'section': [Section.json(sec) for sec in Section.query.filter_by(id=item.section)]
        })

    return jsonify({
        'data': data
    }), 200


@items.get('/<int:id>')
def getItem(id):
    item = Item.query.filter_by(id=id).one()
    data = []

    data.append({
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
        'section': [Section.json(sec) for sec in Section.query.filter_by(id=item.section)]
    })
    
    return jsonify({
        'data': data
    }), 200

    

@items.post('/')
def createItem():
    name = request.json.get('name', '')
    description = request.json.get('description', '')
    price = request.json.get('price', '')
    section = request.json.get('section', '')

    item = Item(name=name, description=description, price=price, section=section)
    db.session.add(item)
    db.session.commit()

    return jsonify({
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
        'section': [Section.json(sec) for sec in Section.query.filter_by(id=item.section)]
    }), 201


@items.put('/<int:id>')
def updateItem(id):
    item_to_update = Item.query.filter_by(id=id).first()
    if item_to_update:
        item_to_update.name = request.json.get('name', '')
        item_to_update.description = request.json.get('description', '')
        item_to_update.price = request.json.get('price', '')
        item_to_update.section = request.json.get('section', '')
        db.session.commit()
        response = Response("Item Updated", status=200, mimetype='application/json')
    else:
        response = Response("Item Not Found", status=404, mimetype='application/json')
    
    return response


@items.delete('/<int:id>')
def deleteItem(id):
    Item.query.filter_by(id=id).delete()
    db.session.commit()
    response = Response("Item Deleted", status=200, mimetype='application/json')

    return response