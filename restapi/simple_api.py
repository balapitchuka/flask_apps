from flask import Flask, jsonify, make_response
from flasgger import Swagger

app = Flask(__name__)

# api documentation(refer /apidocs/)
swagger = Swagger(app)

"""
Api without using any extensions
"""
@app.route('/employees', methods=['GET'])
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