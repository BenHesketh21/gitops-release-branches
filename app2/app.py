from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "App2"

if __name__ == "__main__":
    app.run('0.0.0.0', port=5001)