from marshmallow import Schema, fields, validate


class AnswerReviewSchema(Schema):
    method = fields.String(
        required=True,
        validate=validate.OneOf(
            [
                "FLASHCARD",
                "MULTIPLE_CHOICE",
                "VIETNAMESE_TO_ENGLISH",
                "EXAMPLE_VIETNAMESE_TO_ENGLISH",
            ]
        ),
    )
    is_correct = fields.Boolean(required=True)
