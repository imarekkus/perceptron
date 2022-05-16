"""
This file runs the Flask application we are using as an API endpoint.
"""

from flask import Flask, request, jsonify
import pickle

# Create a flask
app = Flask(__name__)

class Perceptron:
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0, 1, -1)
    
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0, 1, -1)

perceptron = Perceptron()

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
    # Run the app at port 3000
    app.run(port=3000,host='0.0.0.0')
