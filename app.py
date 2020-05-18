from flask import  Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import sort

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/sort', methods=['POST']) 
def flaskLogin():
    if not request.json or not 'UnsortedList' in request.json:
        abort(400) 
    else:
        array = request.json['UnsortedList']
        sort.quickSort(array, 0, len(request.json['UnsortedList']) - 1)
        return jsonify({'sortedList': array}) 

if __name__ == '__main__':
    app.run(debug=True)