# sklearn-flask-docker
An example of deploying a sklearn model using Flask API and a Docker container.

## Steps:

## 1. Create and train the model

I am training a machine learning model using Iris training dataset. To train a new model, run this:

`python model.py`

This outputs a pickle model in a file named `model.pkl`.

## 2. Build a docker image containing Flask and the model

Construct an image (`docker build`) called rafalkaliszczuk/sklearn-flask-docker (`--tag rafalkaliszczuk/sklearn-flask-docker`) from the Dockerfile (`.`).

The construction of this image is defined by `Dockerfile`.

`docker build --tag rafalkaliszczuk/sklearn-flask-docker .`

## 3. Create a container from the Docker Image

Create and start (`docker run`) a detached (`-d`) Docker container called sklearn-flask-docker (`--name sklearn-flask-docker`) from the image `rafalkaliszczuk/sklearn-flask-docker:latest` where port of the host machine is connected to port 5001 of the Docker container.

`docker run -d --name sklearn-flask-docker rafalkaliszczuk/sklearn-flask-docker:latest`

## 4. Query the prediction API with an example observation

Since our model is trained on the Iris dataset, we can test the API by queries it for the predicted class for this example observation:

- sepal length = 1.5
- sepal width = 2.3
- petal length = 1.3
- petal width = 0.3

### In Your Browser

Paste this URL into your browser bar:

http://localhost:5001/predict?sepal_length=1.5&sepal_width=2.3&petal_length=1.3&petal_width=0.3

In your browser you should see something like this:
```
{"features":[1.5,2.3,1.3,0.3],"predicted_class":1}
```

`"predicted_class":1` means that the predicted class is "Iris setosa"
