from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def hey():
    return 'hey, World!'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)