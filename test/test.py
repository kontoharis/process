import unittest
import cv2
import numpy as np
from app import app, changeBrightness, changeBlur

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_changeBrightness(self):
        # Create a sample image
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        brightness_value = 50

        # Apply the brightness change
        adjusted_img = changeBrightness(img, brightness_value)

        # Ensure the output image is not None
        self.assertIsNotNone(adjusted_img)

    def test_changeBlur(self):
        # Create a sample image
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        blur_value = 5

        # Apply the blur operation
        blurred_img = changeBlur(img, blur_value)

        # Ensure the output image is not None
        self.assertIsNotNone(blurred_img)

if __name__ == '__main__':
    unittest.main()
