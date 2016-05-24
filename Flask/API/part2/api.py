from flask import Flask, request
from tinydb import TinyDB, Query

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        print request.json  
        db = TinyDB('db.json')
        db.insert(request.json)
        return "POST Success", 200
    else:
        return "GET Success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)
