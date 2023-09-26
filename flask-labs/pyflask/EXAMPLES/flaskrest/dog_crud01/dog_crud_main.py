#!/usr/bin/env python
import os

def main():
    from flask import Flask, request, jsonify
    app = Flask(__name__)  # needed by other imports

    from flask_restful import Resource, Api, reqparse
    from dog_crud_resources import UserItem, UserCollection

    api = Api(app)

    api.add_resource(UserCollection, '/users')
    api.add_resource(UserItem, '/users/<int:id>')

    app.run(debug=True)


if __name__ == '__main__':
#     if not os.path.exists(db_name):
#         db.create_all()
    main()
