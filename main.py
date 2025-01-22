from flask import Flask, request, jsonify
from app.utils import save_csv, preprocess_data
from app.model import train_model, make_prediction
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'app/data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    save_csv(file, file_path)
    return jsonify({"message": "File uploaded successfully.", "file_path": file_path})

@app.route('/train', methods=['POST'])
def train():
    data_path = os.path.join(UPLOAD_FOLDER, 'dataset.csv')
    if not os.path.exists(data_path):
        return jsonify({"error": "Dataset not found. Please upload a dataset first."}), 400
    
    data = preprocess_data(data_path)
    metrics = train_model(data)
    return jsonify({"message": "Model trained successfully.", "metrics": metrics})

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    if not input_data:
        return jsonify({"error": "No input data provided"}), 400
    
    prediction = make_prediction(input_data)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
