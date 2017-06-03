from flask import Flask, request
from flask_restful import Resource, Api

import json
from bson import ObjectId

from themachine.db.github import User

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    def get(self, username):
        user = User.objects.get(username=username)
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


api.add_resource(UserResource, '/user/<string:username>')
