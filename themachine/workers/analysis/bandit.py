from themachine.core import consumer, publish
from themachine import log
from themachine import util

from themachine.db.github import Repository
from themachine.db.analysis import Report, BanditReport, BanditIssue

import json


@consumer(topic='github.repo_available', name='bandit')
def bandit(data):
    """
    Openstack Bandit consumer.
    Processes a repository and inserts the report in the respository database document.

    :param data:    Dictionary with a repository id key
    """
    repo = Repository.objects.get(**data)

    # only supports Python
    # TODO: use header exchange on rabbitmq for filtering
    if repo.language != 'Python':
        return

    log.info("Analysing repo %s", repo.full_name)

    # run bandit
    p = util.exec(['bandit', '-r', repo.local_path, '-f', 'json'])

    # get output
    result = json.loads(p.stdout)

    # add output to repo object
    report = BanditReport()
    report.severity_high = result['metrics']['_totals']['SEVERITY.HIGH']
    report.severity_medium = result['metrics']['_totals']['SEVERITY.MEDIUM']
    report.severity_low = result['metrics']['_totals']['SEVERITY.LOW']

    report.issues = []
    for bndt_issue in result['results']:
        issue = BanditIssue()
        issue.confidence = bndt_issue['issue_confidence']
        issue.severity = bndt_issue['issue_severity']
        issue.test_id = bndt_issue['test_id']
        issue.test_name = bndt_issue['test_name']
        issue.text = bndt_issue['issue_text']
        issue.save()
        report.issues.append(issue)

    report.save()
    repo.update(add_to_set__reports=report)
