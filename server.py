"""
Flask server for Emotion Detection Web App.
Handles GET requests for analyzing text and displays detected emotions.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)
@app.route("/")
def home():
    """
    Renders the home page with input form for emotion analysis.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Processes the text input via GET request and returns
    the emotion analysis result or an error message.
    """
    text = request.args.get('textToAnalyze')
    if not text:
        return "Invalid text! Please try again!"
    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response_str
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
