from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, ValidationError

ma = Marshmallow()

class SportSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    sport_type = fields.String(required=True)
    age = fields.Integer(required=True)
    description = fields.String(required=True)

__all__ = ['sport_schema', 'sports_schema', 'ValidationError']

sport_schema = SportSchema()
sports_schema = SportSchema(many=True)