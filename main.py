

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return str(dir(request))


if __name__ == '__main__':
    app.run('localhost', port=1337)
