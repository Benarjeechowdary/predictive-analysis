#Predictive Analysis for Manufacturing Operations
This project implements a RESTful API to predict machine downtime using manufacturing data. The API includes endpoints for uploading data, training a model, and making predictions. A simple supervised machine learning model (Decision Tree Classifier) is used for training.

#Features
->Upload Dataset: Accepts a CSV file containing manufacturing data.
->Train Model: Trains a Decision Tree Classifier on the provided dataset.
->Make Predictions: Predicts downtime based on input features.

#Installation
git clone https://github.com/Benarjeechowdary/predictive-analysis.git

#Install dependencies
pip install -r requirements.txt

#run the flask application
python main.py

#API END POINTS
UPLOAD
URL:POST/UPLOAD
COMMAND:curl -X POST -F "file=@app/data/dataset.csv" http://127.0.0.1:5000/upload

TRAIN
URL:POST/train
COMMAND:curl -X POST http://127.0.0.1:5000/train

PREDICT
URL:POST/predict
Example Command:curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 85, "Vibration": 0.6, "Power_Usage": 150, "Humidity": 0.5}' http://127.0.0.1:5000/predict


DATA SET REQUIREMENTS
->Temperature
->Vibration
->Power_Usage
->Humidity
->Downtime
