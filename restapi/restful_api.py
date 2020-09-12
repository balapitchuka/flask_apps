from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

"""
Rest Api using flask-restful extension
"""
class Employee(Resource):
    def get(self):
        return [
            {'name' : 'James'},
            {'name' : 'Ironman'},
        ]

# api urls
api = Api(app)
api.add_resource(Employee, '/employees')

if __name__ == '__main__':
    app.run(debug=True)