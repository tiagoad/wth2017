from mongoengine import *

class User(Document):
    username = StringField(primary_key=True)

    name = StringField()
    email = StringField()
    followers = IntField()

class Repository(Document):
    id = IntField(primary_key=True)
    owner = ReferenceField(User)

    name = StringField()
    full_name = StringField()
    language = StringField()
    git_url = StringField()

    local_path = StringField()
