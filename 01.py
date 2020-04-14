from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от Алисы"


@app.route('/about')
def about():
    return 'Text'


if __name__ == '__main__':
    app.run(host='', port=80)