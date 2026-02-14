"""
Módulo del servidor Flask para la detección de emociones en texto.
Este script maneja las solicitudes y se comunica
con el detector de emociones.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def index():
    """
    Esta función extrae la información de la API
    para mostrar la respuesta en la web
    """

    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = emotions["dominant_emotion"]

    return f"""Para la declaración dada, la respuesta del sistema es
            'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 
            'joy': {joy}, 'sadness': {sadness}. 
            La emoción dominante es {dominant_emotion}"""


@app.route("/")
def render_index_page():
    """
    Renderiza los datos al Front-End
    """
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
