from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/process', methods=["POST"])
def process():
    content = request.json
    data = content["data"]
    print(data)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run(port=8000, debug=True)