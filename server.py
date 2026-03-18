from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid input! Please try again."

    result = emotion_detector(text)

    if "error" in result:
        return "Invalid input! Please try again."

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
