#Ładujemy moduły

from flask import Flask, request, jsonify
import pickle

# Tworzymy flaska
app = Flask(__name__)

# Wklejamy klasę perceptronu bo inaczej nie odpala, a zaimportować też się nie dało
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

# Tworzymy app
@app.route('/')
def home():
    return "Hello, im supposed to return some predictions. Try with data in url link."

@app.route('/predict', methods=['GET'])
def predict():

    # Ustalamy co przyjmuje
    sep_len = float(request.args.get('sepal_length'))
    sep_wid = float(request.args.get('sepal_width'))
    pet_len = float(request.args.get('petal_length'))
    pet_wid = float(request.args.get('petal_width'))
    
    test_data = [sep_len, sep_wid, pet_len, pet_wid]
    
    # Ładujemy zapiklowany model
    perceptron_file = open('model.pkl', 'rb')
    perceptron = pickle.load(perceptron_file)
    perceptron_file.close()
    
     # Predykcja wyniku
    prediction = int(perceptron.predict([test_data]))

    # Wyplucie na stronie predykcji
    return jsonify(features=test_data, predicted_class=prediction)

if __name__ == "__main__":
    # Run the app at port 3000
    app.run(port=3000,host='0.0.0.0')
