from flask import Flask, jsonify, make_response, request
from flasgger import Swagger
from functools import wraps

app = Flask(__name__)

# api documentation(refer /apidocs/)
swagger = Swagger(app)

def authorize(f):
    @wraps(f)
    def decorated_function():
        key = request.args.get('api_key')
        if key == 'abc123':
            return f()
        return jsonify({"statusCode":401, "message":"Un authorised access"})
    return decorated_function

"""
Api without using any extensions
"""
@app.route('/employees', methods=['GET'])
@authorize
def get_all_employees():
    """
    endpoint returns list of employees
    ---
    parameters:
      - name: api_key
        in: query
    responses:
      200:
        description: A list of employees
        examples:
          [{"name" : "Roy"},{"name" : "Sam"}]
    """
    response = make_response(jsonify([{"name" : "James"},{"name" : "Johnson"}]))
    response.headers['Accept-version'] = 'v1'
    return response

@app.errorhandler(404)
def route_not_found(error):
    return jsonify({
        'error' : 'Invalid route',
        'statuscode' : 404,
        })

if __name__ == '__main__':
    app.run(debug=True)