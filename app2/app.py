from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "App2 Hello!!!!!!!!!!!!!"

@app.route('/new')
def new():
    return "App1 Hello!!!!!!!!!!!!!"

@app.route('/new1')
def new1():
    return "App1 Hello!!!!!!!!!!!!!"

if __name__ == "__main__":
    app.run('0.0.0.0', port=5001)