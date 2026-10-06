from marshmallow import Schema, fields, validate


class TopicSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    description = fields.String(allow_none=True)
    vocabulary_count = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class CreateTopicSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    description = fields.String(allow_none=True)


class UpdateTopicSchema(Schema):
    name = fields.String(validate=validate.Length(min=1, max=255))
    description = fields.String(allow_none=True)
