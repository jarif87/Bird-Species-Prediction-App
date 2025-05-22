# app.py
from flask import Flask, request, render_template, url_for
from keras import models
import numpy as np
from PIL import Image
import string
import random
import os

# Initialize Flask app
app = Flask(__name__)

# Set path for file uploads
app.config['INITIAL_FILE_UPLOADS'] = 'static/uploads'

# Ensure uploads directory exists
os.makedirs(app.config['INITIAL_FILE_UPLOADS'], exist_ok=True)

# Load model from model directory
model = models.load_model('model/my_model.keras')

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Default image
    full_filename = 'images/white_bg.jpg'

    # Handle GET request
    if request.method == "GET":
        return render_template("index.html", full_filename=full_filename)

    # Handle POST request
    if request.method == "POST":
        # Check if an image was uploaded
        if 'image_upload' not in request.files:
            return render_template("index.html", full_filename=full_filename, error="No image uploaded")

        image_upload = request.files['image_upload']
        if image_upload.filename == '':
            return render_template("index.html", full_filename=full_filename, error="No image selected")

        # Generate unique image name
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for _ in range(10)) + '.png'
        full_filename = 'uploads/' + name

        # Process and save the image
        try:
            image = Image.open(image_upload)
            image = image.resize((224, 224))
            image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))
            image_arr = np.array(image.convert('RGB'))
            image_arr = image_arr.reshape(1, 224, 224, 3)

            # Predict species
            result = model.predict(image_arr)
            ind = np.argmax(result)
            classes = ['AMERICAN GOLDFINCH','BARN OWL','CARMINE BEE-EATER','DOWNY WOODPECKER','EMPEROR PENGUIN','FLAMINGO']

            # Render template with prediction
            return render_template('index.html', full_filename=full_filename, pred=classes[ind])
        except Exception as e:
            return render_template("index.html", full_filename=full_filename, error=f"Error processing image: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)