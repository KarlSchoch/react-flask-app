import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/jenkins', methods = ['GET'])
def jenkins():
    return {'resp': 'It ran'}

if __name__ == "main":
    app.run()