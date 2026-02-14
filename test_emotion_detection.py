from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detector(unittest.TestCase):

    def test_emotion_detector(self):
        case_1 = emotion_detector("Me alegra que esto haya sucedido")
        self.assertEqual(emotions["dominant_emotion"], "joy")
        case_2 = emotion_detector("Estoy realmente enojado por esto")
        self.assertEqual(emotions["dominant_emotion"], "anger")
        case_3 = emotion_detector("Me siento disgustado solo de escuchar sobre esto")
        self.assertEqual(emotions["dominant_emotion"], "disgust")
        case_4 = emotion_detector("Estoy muy triste por esto")
        self.assertEqual(emotions["dominant_emotion"], "sadness")
        case_5 = emotion_detector("Tengo mucho miedo de que esto suceda")
        self.assertEqual(emotions["dominant_emotion"], "fear")


unittest.main()    