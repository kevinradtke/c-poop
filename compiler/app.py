from flask import Flask, request
from flask_cors import CORS
import os
import sys


app = Flask(__name__)
CORS(app)


def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)


@app.route('/reset', methods=['GET'])
def hello_world():
    return reset()


@app.route('/compile', methods=["POST"])
def compile():
    code = request.form['code']
    file = open("copy.txt", "w")
    file.write(code)
    file.close()

    import vm
    vm.flask_comp_and_run("copy.txt")

    return open("ide_output.txt", "r").read()


if __name__ == '__main__':
    app.run(debug=True)
