import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):    
    def get_emotion(self, emotion_dict):
        value = 0
        feeling = ''
        for emotion, num in emotion_dict.items():
            if num > value:
                value = num
                feeling = emotion
        return feeling

    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")
        emotion = self.get_emotion(result)
        self.assertEqual(emotion, "joy")

        result = emotion_detector("I am really mad about this")
        emotion = self.get_emotion(result)
        self.assertEqual(emotion, "anger")

        result = emotion_detector("I feel disgusted just hearing about this")
        emotion = self.get_emotion(result)
        self.assertEqual(emotion, "disgust")

        result = emotion_detector("I am so sad about this")
        emotion = self.get_emotion(result)
        self.assertEqual(emotion, "sadness")

        result = emotion_detector("I am really afraid that this will happen")
        emotion = self.get_emotion(result)
        self.assertEqual(emotion, "fear")

if __name__ == '__main__':
    unittest.main()
