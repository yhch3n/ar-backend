"""Modules containing all request/response schemas."""
from marshmallow import Schema, fields


class ArDataSchema(Schema):
    """Response schema for get projects API."""

    class Meta:
        ordered = True

    roomId = fields.String()
    keyword = fields.String()
    modelMatrix = fields.String()
    anchorPose = fields.String()
    hashcode = fields.String()
