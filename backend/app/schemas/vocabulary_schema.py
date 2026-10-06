from marshmallow import Schema, fields, validate


class VocabularySchema(Schema):
    id = fields.Integer(dump_only=True)
    topic_id = fields.Integer(required=True)
    word = fields.String(required=True, validate=validate.Length(min=1, max=255))
    meaning = fields.String(required=True, validate=validate.Length(min=1))
    ipa_uk = fields.String(allow_none=True)
    ipa_us = fields.String(allow_none=True)
    example_en = fields.String(allow_none=True)
    example_vn = fields.String(allow_none=True)
    progress = fields.Dict(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class CreateVocabularySchema(Schema):
    topic_id = fields.Integer(required=True)
    word = fields.String(required=True, validate=validate.Length(min=1, max=255))
    meaning = fields.String(required=True, validate=validate.Length(min=1))
    ipa_uk = fields.String(allow_none=True)
    ipa_us = fields.String(allow_none=True)
    example_en = fields.String(allow_none=True)
    example_vn = fields.String(allow_none=True)


class UpdateVocabularySchema(Schema):
    word = fields.String(validate=validate.Length(min=1, max=255))
    meaning = fields.String(validate=validate.Length(min=1))
    ipa_uk = fields.String(allow_none=True)
    ipa_us = fields.String(allow_none=True)
    example_en = fields.String(allow_none=True)
    example_vn = fields.String(allow_none=True)
