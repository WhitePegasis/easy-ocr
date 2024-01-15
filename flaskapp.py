from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

import easyocr
import os
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/process_image', methods=['POST'])
def process_image():
    print("Got a hit...")

    try:
        print("Trying")
        print(request)
        image_data = request.files['image'].read()
        # print(image_data)
        print(type(image_data))

        # Save image to a temporary file
        temp_dir = tempfile.gettempdir()
        image_path = os.path.join(temp_dir, 'temp_image.png')

        with open(image_path, 'wb') as temp_file:
            temp_file.write(image_data)

        # Perform OCR on the saved image
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image_path)
        string_values = [item[1] for item in result]

        print(string_values)

        return jsonify({'result': str(string_values)})

    except Exception as e:
        print("Got an error")
        print(e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
