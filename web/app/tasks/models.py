# coding=utf-8

from geoalchemy2 import Geometry
from app import db
from .serializers import TaskSerializer


class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    point = db.Column(
        Geometry('POINT'),
        nullable=False
    )
    date_created = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )
    message = db.Column(
        db.String(256),
        nullable=False
    )
    priority = db.Column(
        db.SmallInteger,
        default=0
    )

    def serialize(self):
        serializer = TaskSerializer()
        result = serializer.dump(self)
        return result.data

    @classmethod
    def create(cls, **kwargs):
        task = cls()
        task.priority = kwargs.get('priority', 0)
        task.message = kwargs.get('message', '')
        location = kwargs.get('location')
        task.point = u"POINT({} {})".format(location['lat'], location['lng'])
        return task
