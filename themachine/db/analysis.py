from mongoengine import *

class Issue(Document):
    meta = {'allow_inheritance': True}

    severity = StringField()
    confidence = StringField()

class Report(Document):
    meta = {'allow_inheritance': True}
    type = 'generic'

    score = IntField()
    issues = ListField(ReferenceField(Issue))

class BanditIssue(Issue):
    text = StringField()
    test_id = StringField()
    test_name = StringField()

class BanditReport(Report):
    severity_high = IntField()
    severity_medium = IntField()
    severity_low = IntField()

class PEP8Report(Report):
    stats = StringField()

