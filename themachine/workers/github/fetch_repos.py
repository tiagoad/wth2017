from themachine.core import consumer, publish
from themachine import log
import tempfile

from themachine.db.github import Repository

import git
import github

@consumer(topic='github.fetch_repo', name='fetch_repo')
def fetch_repo(data):
    repo = Repository.objects.get(**data)
    log.info("Fetching %s's repo %s", repo.owner.username, repo.full_name)

    # create a temporary directory
    tmp_dir = tempfile.mkdtemp('github')

    # clone the repository to the directory
    git.Repo.clone_from(repo.git_url, tmp_dir)
