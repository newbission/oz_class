from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str(required=True)
    password = fields.Str(required=True)

class UserCreateSchema(UserSchema):
    pass

class UserUpdateSchema(UserSchema):
    id = fields.Int(dump_only=True)