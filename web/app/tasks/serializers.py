# coding=utf-8

from marshmallow import Schema, fields
from shapely import wkb


class TaskSerializer(Schema):

    class Meta:
        fields = (
            'id', 'href', 'location', 'message', 'priority',
            'date_created',
        )

    location = fields.Method("get_location")
    href = fields.Method('get_href')

    def get_location(self, obj):
        point = wkb.loads(bytes(obj.point.data))
        return {'lat': point.x, 'lng': point.y}

    def get_href(self, obj):
        return obj.id
