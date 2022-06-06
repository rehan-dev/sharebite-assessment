from flask_sqlalchemy import SQLAlchemy
import string
from sqlalchemy.orm import backref, relationship

db = SQLAlchemy()


item_modifier = db.Table('item_modifier',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('modifier_id', db.Integer, db.ForeignKey('modifiers.id'))
)

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

    def __repr__(self) -> str:
        return 'Section >>> {self.name}'


class Modifiers(db.Model):
    __tablename__ = 'modifiers'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.description}

    def __repr__(self) -> str:
        return 'Modifier >>> {self.description}'


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.DECIMAL(10,2), nullable=False)
    section = db.Column(db.Integer, db.ForeignKey("section.id"))
    # modifiers = db.Column(db.Integer, db.ForeignKey("modifiers.id"))
    modifiers = db.relationship('Modifiers', secondary=item_modifier, backref="item_modifiers")

    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'price': self.price}
        
    def Itemjson(self):
        return {'id': self.id, 'title': self.name, 'modifiers': [Modifiers.json(mod) for mod in self.modifiers]}
    
    def __repr__(self) -> str:
        return 'Item >>> {self.name}'
