from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'INDEX3'


@app.route('/compile', methods=["POST"])
def compile():
    code = request.form['code']
    print(code)
    return "print('test');"


if __name__ == '__main__':
    app.run(debug=True)
