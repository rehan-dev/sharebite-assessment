from flask import Blueprint, request, jsonify, Response, json
from src.database import Section, Item, Modifiers, db

restaurantmenu = Blueprint("restaurantmenu", __name__, url_prefix="/api/v1/menu")

@restaurantmenu.get('/')
def menu():
    data = []

    sections = Section.query.all()
    for sec in sections:
        data.append({
            'id': sec.id,
            'title': sec.name,
            'items': [Item.Itemjson(itm) for itm in Item.query.filter_by(section=sec.id)]
        })

    return jsonify({
        'data': data
    }), 200