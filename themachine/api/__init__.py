from flask import Flask, request
from flask_restful import Resource, Api, abort

from themachine.db.github import User

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    # PROOF OF CONCEPT
    def get(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            abort(404, message='No such user')

        user_dict = user.to_mongo().to_dict()
        del user_dict['_id']

        user_dict['repositories'] = []
        for repo in user.repositories:
            repo_dict = repo.to_mongo().to_dict()
            del repo_dict['_id']
            user_dict['repositories'].append(repo_dict)

            repo_dict['reports'] = []
            for report in repo.reports:
                report_dict = report.to_mongo().to_dict()
                del report_dict['_id']
                repo_dict['reports'].append(report_dict)

                report_dict['issues'] = []
                for issue in report.issues:
                    issue_dict = issue.to_mongo().to_dict()
                    del issue_dict['_id']
                    report_dict['issues'].append(issue_dict)

        return user_dict

    def post(self, username):
        from themachine.core import publish

        publish('github.start_user_process', {
            'username': username
        })

api.add_resource(UserResource, '/user/<string:username>')
