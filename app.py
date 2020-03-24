from flask import  Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import sort

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/') # simple index method
def index():
    return "Edaa35 test application"

@app.route('/api/test') # returnning a simple json
def getTestjson():
    return jsonify({'Test': 'testing'})

@app.route('/api/sort', methods=['POST']) 
def flaskLogin():
    print(request.json['UnsortedList'])
    if not request.json or not 'UnsortedList' in request.json:
        abort(400) 
    else:
        array = request.json['UnsortedList']
        sort.quickSort(array, 0, len(request.json['UnsortedList']) - 1)
        return jsonify({'sortedList': array}) 

@app.errorhandler(404) # error handler to answer 404 with json
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)