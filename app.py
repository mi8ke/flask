# app.py

from flask import Flask, request, render_template, url_for
import os
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    # Save the uploaded image
    image_path = os.path.join('uploads', file.filename)
    file.save(image_path)
    
    # Perform image processing (convert to grayscale)
    processed_image_path = os.path.join('uploads', 'processed_' + file.filename)
    img = Image.open(image_path).convert('L')
    img.save(processed_image_path)
    
    return render_template('index.html', processed_image_path=processed_image_path)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
