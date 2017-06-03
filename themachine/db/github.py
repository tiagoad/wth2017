from mongoengine import *

from themachine.db.analysis import Report

class Repository(Document):
    """
    GitHub repository
    """
    id = IntField(primary_key=True)

    name = StringField()
    full_name = StringField()
    language = StringField()
    git_url = StringField()

    local_path = StringField()

    reports = ListField(ReferenceField(Report))

class User(Document):
    """
    GitHub user
    """
    username = StringField()
    name = StringField()
    email = StringField()
    followers = IntField()

    repositories = ListField(ReferenceField(Repository))

