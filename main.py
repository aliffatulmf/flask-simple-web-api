from flask import Flask, jsonify, make_response, request
from data import MANGA_LIST
from lib import parallel, validation

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"


@app.route("/api/v1/manga", methods=["GET"])
def api_manga_all():
    return make_response(jsonify({"data": MANGA_LIST}), 200)


@app.route("/api/v1/manga/find/<int:id>", methods=["GET"])
def api_manga_find(id):
    n = parallel.parallel_search(iter=MANGA_LIST, value=id)
    if len(n) == 0:
        return make_response(
            jsonify({
                "type": "error",
                "message": "data not found",
            }), 400)

    return make_response(jsonify(n[0]), 200)


@app.route("/api/v1/manga/add", methods=["POST"])
def api_manga_post():
    schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "number"
            },
            "name": {
                "type": "string"
            },
            "myanimelist": {
                "rating": {
                    "type": "number"
                },
                "ranked": {
                    "type": "number"
                },
                "popularity": {
                    "type": "number"
                },
                "studio": {
                    "type": "string"
                }
            }
        }
    }

    j = request.get_json()
    v = validation.jsonvalidator(schema=schema, json=j)
    s = 201

    if not v:
        j = {
            "type": "error",
            "message": "data not valid",
        }
        s = 400

    res = make_response(jsonify(j), s)
    return res


@app.route("/api/v1/manga/destroy/<int:id>", methods=["DELETE"])
def api_manga_destroy(id):
    n = parallel.parallel_search(iter=MANGA_LIST, value=id)

    if len(n) == 0:
        return make_response(
            jsonify({
                "type": "error",
                "message": "data not found",
            }), 400)

    return make_response("", 204)


if __name__ == "__main__":
    app.run()
