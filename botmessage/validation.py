from marshmallow import Schema, fields, validate

class SendMessageSchema(Schema):
    message = fields.Str(required=True, validate=validate.Length(max=500))
