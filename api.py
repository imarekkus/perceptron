"""
This file runs the Flask application we are using as an API endpoint.
"""

from flask import Flask, request, jsonify
import pickle

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/')
def home():
    return "Hi, Welcome to Flask!!"

@app.route('/predict', methods=['GET'])
def predict():

    # Getting features values e.g.
    #/predict?sepal_length=4.5&sepal_width=2.3&petal_length=1.3&petal_width=0.3
    sep_len = float(request.args.get('sepal_length'))
    sep_wid = float(request.args.get('sepal_width'))
    pet_len = float(request.args.get('petal_length'))
    pet_wid = float(request.args.get('petal_width'))
    
    # The features of the observation to predict
    test_data = [sep_len, sep_wid, pet_len, pet_wid]
    
    # Load pickled model file
    perceptron_file = open('model.pkl', 'rb')
    perceptron = pickle.load(perceptron_file)
    perceptron_file.close()
    
     # Predict the class using the model
    prediction = int(perceptron.predict([test_data]))

    # Return a json object containing the features and prediction
    return jsonify(features=test_data, predicted_class=prediction)

if __name__ == "__main__":
    # Run the app at port 5001
    app.run(port=5001)
