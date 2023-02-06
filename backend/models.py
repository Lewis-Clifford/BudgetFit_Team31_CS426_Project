from marshmallow import Schema, fields

class Item(object):

    def __init__(self, name, price, store, type):
        self.name = name
        self.price = price
        self.store = store
        self.type = type

    def __repr__(self):

        return '<Item(name={self.name!r}'.format(self=self)

class ItemSchema(Schema):
    name = fields.Str()
    price = fields.Number()
    store = fields.Str()
    type = fields.Str()