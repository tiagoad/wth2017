from themachine.core import consumer, publish
from themachine import log
from themachine import util

from themachine.db.github import Repository
from themachine.db.analysis import Report, BanditReport, BanditIssue

import json


@consumer(topic='github.repo_available', name='bandit')
def bandit(data):
    repo = Repository.objects.get(**data)

    # only supports Python
    # TODO: use header exchange on rabbitmq for filtering
    if repo.language != 'Python':
        return

    log.info("Analysing %s's repo %s", repo.owner.username, repo.full_name)

    # run bandit
    p = util.exec(['bandit', '-r', repo.local_path, '-f', 'json'])

    # get output
    result = json.loads(p.stdout)

    # add report
    report = BanditReport()
    report.severity_high = result['metrics']['_totals']['SEVERITY.HIGH']
    report.severity_medium = result['metrics']['_totals']['SEVERITY.MEDIUM']
    report.severity_low = result['metrics']['_totals']['SEVERITY.LOW']
    report.repo = repo
    report.save()

    # add report issues
    for bndt_issue in result['results']:
        issue = BanditIssue()
        issue.report = report
        issue.confidence = bndt_issue['issue_confidence']
        issue.severity = bndt_issue['issue_severity']
        issue.test_id = bndt_issue['test_id']
        issue.test_name = bndt_issue['test_name']
        issue.text = bndt_issue['issue_text']
        issue.save()
