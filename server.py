"""Flask web interface for the Emotion Detector."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Validate user input and return emotion analysis."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please enter a sentence and try again.", 400

    try:
        result = emotion_detector(text_to_analyze)
    except (ValueError, KeyError, IndexError, TypeError):
        app.logger.exception("The emotion service returned an invalid response.")
        return "Emotion detection could not process that text. Please try again.", 502
    except Exception:
        app.logger.exception("The emotion service request failed.")
        return "Emotion detection service is unavailable. Please try again later.", 502

    if result is None:
        return "Emotion detection could not process that text. Please try again.", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
