import requests 
import json

def emotion_detector(text_to_analyze):
    """
    Analiza las emociones presentes en un texto dado.

    Recibe una cadena de caracteres y determina si el sentimiento predominante
    es positivo, negativo o neutral

    Args:
        text_to_analyze (str): El texto que se someterá al análisis.

    Returns:
        json: Analisis de sentimientos
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post (url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        emotions = response_json["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
        return emotions
        
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


