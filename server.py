"""
Flask application for Emotion Detection
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_page():
    """Render the main page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def display_emotion():
    """
    Process the text input and return emotion analysis results
    """
    # Getting the text
    sent = request.args.get("textToAnalyze")

    # Adding the text to the emotion detector function
    result = emotion_detector(sent)

    # Check if result is None or contains None values
    if result is None:
        return "Invalid input! Try again."

    # Check for None values in emotions
    if any(value is None for value in result.values()):
        return "Invalid input! Try again."

    # Initial output result
    output = "For the given statement, the system response is "
    max_value = 0
    dominant_emotion = ''

    for emotion, num in result.items():
        if emotion != 'sadness':
            output = output + emotion + ': ' + str(num) + ', '
        else:
            output = output + emotion + ': ' + str(num) + '. '

        if num > max_value:
            max_value = num
            dominant_emotion = emotion

    output = output + f'The dominant emotion is {dominant_emotion}.'
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)