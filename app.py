from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the index"

@app.route("/hello/<nome>")
def hello(nome=""):
    return "<h2> Hello, {} </h2>".format(nome)


if __name__ == '__main__':
    app.run()