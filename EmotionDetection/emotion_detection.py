import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    if text_to_analyze=='':
       emotions = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None} 
    elif response.status_code == 200:
		# Parse the response from the API
		formatted_response = json.loads(response.text)
		emotions=result['emotionPredictions'][0]['emotion']
	# If the response status code is 500, set label and score to None
	elif response.status_code == 500:
		emotions = None
	# For any other unexpected status codes, set label and score to None
	else:
		emotions = None
    return emotions