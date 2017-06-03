from themachine.core import consumer, publish
from themachine import log
from themachine.db import get_or_create
from themachine.db.github import User, Repository

import os
import github

@consumer(topic='github.start_user_process', name='fetch_metadata')
def fetch_metadata(data):
    log.info('Fetching metadata for GitHub user %s', data['username'])

    gh = github.Github(os.getenv('GITHUB_TOKEN'))
    gh_user = gh.get_user(data['username'])

    user = get_or_create(User, username=data['username'])
    user.username = data['username']
    user.name = gh_user.name
    user.email = gh_user.email
    user.followers = gh_user.followers
    user.save()

    repo_type = os.getenv('GITHUB_REPO_TYPES')
    log.info('Fetching repositories of type %s' % repo_type)

    for gh_repo in gh_user.get_repos(type=repo_type):
        if gh_repo.fork and os.getenv('GITHUB_NO_FORKS') == '1':
            continue

        repo = get_or_create(Repository, id=gh_repo.id)
        repo.language = gh_repo.language
        repo.git_url = gh_repo.git_url

        repo.name = gh_repo.name
        repo.full_name = gh_repo.full_name

        repo.save()
        user.update(add_to_set__repositories=repo)

        publish('github.fetch_repo', {
            'id': gh_repo.id
        })
