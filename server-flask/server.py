from flask import Flask, request, jsonify
from ga import get_best_individual


app = Flask(__name__)


@app.route('/process', methods=["POST"])
def process():
    bestindividual = get_best_individual()
    result = {"data": bestindividual}

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8000,
            debug=True, threaded=False)