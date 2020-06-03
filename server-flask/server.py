from flask import Flask, request, jsonify
from ga import get_best_individual


app = Flask(__name__)


@app.route('/process', methods=["POST"])
def process():
    content = request.json
    data = content["data"]
    # print("Input data:", data)

    bestindividual = get_best_individual()
    # print(n_primes)
    # print(primes)

    result = {"bestindividual": bestindividual,
             }

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8000,
            debug=True)