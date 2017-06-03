from mongoengine import *

class Issue(Document):
    """
    Generic issue found by an analysis tool
    """
    meta = {'allow_inheritance': True}

    severity = StringField()
    confidence = StringField()

class Report(Document):
    """
    Generic analysis report
    """
    meta = {'allow_inheritance': True}
    type = 'generic'

    score = IntField()
    issues = ListField(ReferenceField(Issue))

class BanditIssue(Issue):
    """
    Bandit issue
    """
    text = StringField()
    test_id = StringField()
    test_name = StringField()

class BanditReport(Report):
    """
    Bandit report
    """
    severity_high = IntField()
    severity_medium = IntField()
    severity_low = IntField()

class PEP8Report(Report):
    """
    PEP8 Report
    """
    stats = StringField()

