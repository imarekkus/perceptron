# sklearn-flask-docker
An example of deploying a sklearn model using Flask API and a Docker container.

## Steps:

## 1. Create and train the model

I am training a machine learning model using Iris training dataset. To train a new model, run this:

`python model.py`

This outputs a pickle model in a file named `model.pkl`.

## 2. Build a docker image containing Flask and the model

Construct an image (`docker build`) called imarekkus/peceptron (`--tag imarekkus/peceptron`) from the Dockerfile (`.`).

The construction of this image is defined by `Dockerfile`.

`docker build --tag imarekkus/perceptron .`

## 3. Create a container from the Docker Image

Create and start (`docker run`) a detached (`-d`) Docker container called sklearn-flask-docker (`--name sklearn-flask-docker`) from the image `imarekkus/perceptron:latest` where port of the host machine is connected to port 3000 of the Docker container.

`docker run -d --name sklearn-flask-docker imarekkus/perceptron:latest`

## 4. Query the prediction API with an example observation

Since our model is trained on the Iris dataset, we can test the API by queries it for the predicted class for this example observation:

- sepal length = 1.5
- sepal width = 2.3
- petal length = 1.3
- petal width = 0.3

### In Your Browser

Paste this URL into your browser bar:

http://localhost:3000/predict?sepal_length=1.5&sepal_width=2.3&petal_length=1.3&petal_width=0.3

In your browser you should see something like this:
```
{"features":[1.5,2.3,1.3,0.3],"predicted_class":1}
```

`"predicted_class":1` means that the predicted class is "Iris setosa"
