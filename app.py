from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import predict_next_words
from grammar_model import correct_grammar

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    predictions = predict_next_words(input_text)
    return jsonify({"predictions": predictions})

@app.route("/correct", methods=["POST"])
@app.route("/correct", methods=["POST"])
@app.route("/correct", methods=["POST"])
def correct():
    data = request.json
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    corrected_text = correct_grammar(input_text)
    return jsonify({"corrected_text": corrected_text})



if __name__ == "__main__":
    app.run(debug=True)