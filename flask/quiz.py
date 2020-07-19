from flask import Flask
import import_ipynb
from src import newfile
from os import path, walk
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/new')
def hey():
    return 'hey, World!'

# new api added
@app.route('/counter')
def counter():
    count = newfile.getCounter()
    print("count", count)
    return count

if __name__ == '__main__':
    app.run()