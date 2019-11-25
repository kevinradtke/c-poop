from flask import Flask, request, current_app
from vm import flask_comp_and_run
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'INDEX3'


@app.route('/compile', methods=["POST"])
def run_api():

    code = request.form['code']

    file = open("translated_code.txt", "w")
    file.write(code)
    file.close()

    flask_comp_and_run("translated_code.txt")

    with current_app.open_resource('ide_output.txt') as f:
        return f.read()


if __name__ == '__main__':
    app.run(debug=True)
