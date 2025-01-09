from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Ensure app is initialized correctly (import app if it's in a separate module)
from app import app  # Assuming app is defined in app.py or __init__.py

# Define the upload folder and allowed file extensions
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # Retrieve form data
        data = request.form.to_dict()  # Extract form data as a dictionary
        photo = request.files.get('photo')  # Get the uploaded photo

        # Save photo if valid
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)  # Sanitize filename
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the photo
            data['photo_path'] = filename  # Add photo path to the data dictionary
        else:
            return jsonify({"status": "error", "message": "Invalid file!"}), 400

        # Optionally, store form data (e.g., save to a database or a file)
        with open('submitted_data.txt', 'a') as f:
            f.write(str(data) + '\n')  # Append form data to the file

        return jsonify({"status": "success", "message": "Form submitted successfully!"})

    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({"status": "error", "message": str(e)}), 500
