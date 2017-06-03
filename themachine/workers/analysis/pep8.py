from themachine.core import consumer, publish
from themachine import log
from themachine import util

from themachine.db.github import Repository
from themachine.db.analysis import PEP8Report

@consumer(topic='github.repo_available', name='ppe8')
def bandit(data):
    repo = Repository.objects.get(**data)

    # only supports Python
    # TODO: use header exchange on rabbitmq for filtering
    if repo.language != 'Python':
        return

    log.info("Analysing repo %s", repo.full_name)

    # run pep8
    p = util.exec(['pep8', '--statistics', repo.local_path])

    report = PEP8Report()
    report.stats = p.stdout.decode('utf-8')
    report.save()

    repo.update(add_to_set__reports=report)
