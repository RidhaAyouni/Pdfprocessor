# from flask import request, jsonify, Blueprint
# from services import pdf_to_structured_text, convert_text_to_table, transform_df_to_json, send_data_to_microservice
# import os
# from flask import Flask

# app = Flask(__name__)
# @app.route('/home')
# def home():
#     return "Hello, World!"

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
    
#     if file and allowed_file(file.filename):
#         file_path = os.path.join('/path/to/save', file.filename)
#         file.save(file_path)
        
#         text = pdf_to_structured_text(file_path)
#         df = convert_text_to_table(text)
#         data_json = transform_df_to_json(df)
#         response = send_data_to_microservice(data_json)
        
#         return jsonify({"status": response.status_code, "data": response.json()})

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import os
import pandas as pd
from decimal import Decimal
import pdfplumber
import requests
import json
from werkzeug.utils import secure_filename

# Import service functions from a separate module
from services import pdf_to_structured_text, convert_text_to_table, transform_df_to_json, send_data_to_microservice

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Process the PDF
        structured_text = pdf_to_structured_text(file_path)
        df = convert_text_to_table(structured_text)
        data_json = transform_df_to_json(df)
        
        
        # Send the JSON data to the Spring Boot service
        #response = send_data_to_microservice(data_json)
        
        return data_json, 200
    
    return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

