from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    x = request.json["x"]
    y = model.predict([[x]])
    return jsonify({"prediction": float(y[0])})

app.run(host="0.0.0.0", port=5000)
