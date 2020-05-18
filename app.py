from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    response =  render_template('index.html', msg='hello world')
    return response


@app.route('/api', methods=['GET'])
def api():
    response = jsonify({'response':'hello world'})
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
