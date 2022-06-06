from flask import Blueprint, request, jsonify, Response
from src.database import Section, Item, Modifiers, db

mapper = Blueprint("mapper", __name__, url_prefix="/api/v1/mapper")


@mapper.post('/')
def mapItemModifier():
    item_id = request.json.get('item_id', '')
    modifier_id = request.json.get('modifier_id', '')

    modifier = Modifiers.query.filter_by(id=modifier_id).first()
    item = Item.query.filter_by(id=item_id).first()


    item.modifiers.append(modifier)
    db.session.commit()

    response = Response("Modifier Map with Item", status=201, mimetype='application/json')
    
    return response