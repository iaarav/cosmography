from flask import Flask

app = Flask(__name__)


@app.route('/main')
def index():
    return "Yo, you're cool if you're seeing this"


if __name__ == '__main__':
    app.run(debug=True)
