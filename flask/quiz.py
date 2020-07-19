from flask import Flask
import import_ipynb
from src import newfile
from os import path, walk

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/new')
def hey():
    return 'hey, World!'

# new api added
@app.route('/counter')
def counter():
    count = 5
    return newfile.getCounter()

if __name__ == '__main__':
    app.run()