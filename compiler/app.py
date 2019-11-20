from flask import Flask, request, current_app
from vm import comp_and_run
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'INDEX3'


@app.route('/compile')
def run_api():
    # comp_and_run()
    with current_app.open_resource('ide_output.txt') as f:
        return f.read()


if __name__ == '__main__':
    app.run(debug=True)
