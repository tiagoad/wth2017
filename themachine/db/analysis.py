from mongoengine import *
from themachine.db.github import Repository

from enum import Enum

class Report(Document):
    meta = {'allow_inheritance': True}

    repo = ReferenceField(Repository)
    score = IntField()

class BanditReport(Report):
    severity_high = IntField()
    severity_medium = IntField()
    severity_low = IntField()

class BanditIssue(Document):
    report = ReferenceField(BanditReport)

    severity = StringField()
    confidence = StringField()
    text = StringField()
    test_id = StringField()
    test_name = StringField()
