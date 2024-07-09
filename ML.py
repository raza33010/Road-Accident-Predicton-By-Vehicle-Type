from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import joblib

app = Flask(__name__)
CORS(app)

# Load your trained machine learning model


@app.route('/DT_py/predict', methods=['POST'])
def predict():
    try:
        # Get data from JSON request
        data = request.get_json()

        # Extract features dynamically from JSON
        features = [float(data.get(key)) for key in data.keys()]  # Assuming all values are float

        # Convert features to numpy array and reshape as needed
        features = np.array(features).reshape(1, -1)
        model = pickle.load(open('DT.pkl', 'rb'))
        # Make prediction
        prediction = model.predict(features)
        if prediction == 1:
            response = {'prediction': "cars"}
        elif prediction ==4 :
            response = {'prediction': "Taxi"}
        else:
        # Prepare response in JSON format
            response = {'prediction': "Others"}  # Assuming prediction is integer type

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message with 400 status code on exception
    
    


@app.route('/LR_py/predict', methods=['POST'])
def predictRL():
    try:
        # Get data from JSON request
        data = request.get_json()

        # Extract features dynamically from JSON
        features = [float(data.get(key)) for key in data.keys()]  # Assuming all values are float

        # Convert features to numpy array and reshape as needed
        features = np.array(features).reshape(1, -1)
        # Load your trained machine learning model
        model = joblib.load('regressor.pkl')
        # Make prediction
        prediction = model.predict(features)
        if prediction == 1:
            response = {'prediction': "cars"}
        elif prediction ==4 :
            response = {'prediction': "Taxi"}
        else:
        # Prepare response in JSON format
            response = {'prediction': "Others"}  # Assuming prediction is integer type

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message with 400 status code on exception
    


@app.route('/DT/predict', methods=['POST'])
def predictwithoutpy():
    try:
        # Get data from JSON request
        data = request.get_json()

        # Extract features dynamically from JSON
        features = [float(data.get(key)) for key in data.keys()]  # Assuming all values are float

        # Convert features to numpy array and reshape as needed
        features = np.array(features).reshape(1, -1)
        model = joblib.load('DT_py.pkl')
        # Make prediction
        prediction = model.predict(features)
        if prediction == 1:
            response = {'prediction': "cars"}
        elif prediction ==4 :
            response = {'prediction': "Taxi"}
        else:
        # Prepare response in JSON format
            response = {'prediction': "Others"}  # Assuming prediction is integer type

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message with 400 status code on exception    


if __name__ == '__main__':
    app.run(debug=True)


