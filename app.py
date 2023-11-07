from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    time.sleep(5)
    return '[{"nome": "Delano"}, {"nome": "Joao"}]'

if __name__ == '__main__':
    app.run(host='0.0.0.0')