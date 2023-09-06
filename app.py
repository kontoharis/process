from flask import Flask, render_template, request, Response
import cv2
import numpy as np
import pyshine as ps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def changeBrightness(img, value):
    """ This function will take an image (img) and the brightness
        value. It will perform the brightness change using OpenCV
        and return the adjusted image.
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def changeBlur(img, value):
    """ This function will take the img image and blur values as inputs.
        After performing a blur operation using OpenCV, it returns
        the image img.
    """
    kernel_size = (value + 1, value + 1)  # +1 is to avoid 0
    img = cv2.blur(img, kernel_size)
    return img

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            brightness_value_now = int(request.form['brightness'])
            blur_value_now = int(request.form['blur'])
            img = changeBrightness(img, brightness_value_now)
            img = changeBlur(img, blur_value_now)

            # Encode the processed image to JPEG format for display
            _, encoded_img = cv2.imencode('.jpg', img)

            return Response(encoded_img.tobytes(), mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True,threaded=True,host='13.51.204.248')