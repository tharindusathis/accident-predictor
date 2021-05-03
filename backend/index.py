from flask import Flask, jsonify, Response, request
import predictor

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getme():
    return str('Backend is live 🗺')


@app.route('/api/sample', methods=['GET'])
def sample():
    return jsonify(predictor.predict_input_sample)


@app.route('/api/predict', methods=['GET'])
def predict():
    request_data = request.get_json()
    return jsonify(predictor.predict(request_data))


@app.route('/api', methods=['GET', 'POST'])
def api():
    method = ""
    if request.method == "POST":
        method = "Post"
    else:
        method = "Get"
    return jsonify({"method": method})
