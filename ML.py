from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

# Load your trained machine learning model
model = pickle.load(open('DT.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from JSON request
        data = request.get_json()

        # Extract features dynamically from JSON
        features = [float(data.get(key)) for key in data.keys()]  # Assuming all values are float

        # Convert features to numpy array and reshape as needed
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Prepare response in JSON format
        response = {'prediction': int(prediction[0])}  # Assuming prediction is integer type

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message with 400 status code on exception

if __name__ == '__main__':
    app.run(debug=True)
