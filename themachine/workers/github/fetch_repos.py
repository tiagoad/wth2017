from themachine.core import consumer, publish
from themachine import log
from themachine import util
import tempfile

from themachine.db.github import Repository

import git
import os

@consumer(topic='github.fetch_repo', name='fetch_repo')
def fetch_repo(data):
    repo = Repository.objects.get(**data)

    # create a temporary directory
    tmp_dir = util.tmp_dir('github')

    # log
    log.info("Fetching repo %s to %s", repo.full_name, tmp_dir)

    # clone the repository to the directory
    git.Repo.clone_from(repo.git_url, tmp_dir)

    # add the repo path to the database
    repo.local_path = tmp_dir
    repo.save()

    # tell workers the repo is available
    publish('github.repo_available', data)
