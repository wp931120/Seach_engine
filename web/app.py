from flask import request, Flask, jsonify
from search.Searchengine import Searchengine
from flask_cors import *


app = Flask(__name__)

CORS(app, supports_credentials=True)
searchengine = Searchengine()


@app.route("/")
def main():
    return "hello world"


@app.route("/search", methods=["GET","POST"])
def search():
    reponsedic = {}
    data = request.form.get("data", type=str,default=None)
    response = searchengine.search(data)
    reponsedic["data"]  =response
    return jsonify(reponsedic), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)




