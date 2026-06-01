from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detection")

@app.route("/")
def render_page():
    return render_template("index.html")

@app.route("/detect")
def display_emotion():
    #Getting the text
    sent=request.args.get("textToAnalyze")

    #Adding the text to the emotion detector function
    result=emotion_detector(sent)

    # Initial output result
    output="For the given statement, the system response is "
    value=0
    feeling=''
    for emotion,num in emotion_dict.items():
        if not emotion=='sadness':
            output=output+ emotion+': '+num+', '
        else:
            output=output+ emotion+': '+num+'. '
        if num>value:
            value=num
            feeling=emotion

    output= output+f'The dominant emotion is {feeling}.'
    return output