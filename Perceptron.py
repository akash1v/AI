import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=1000):

        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def predict(self, X):
        y = np.dot(X, self.weights) + self.bias
        return self.sigmoid(y)


    def fit(self, X, y):

        samples, features = X.shape
        self.weights = np.zeros(features)
        self.bias = 0

        for epoch in range(self.epochs):
            for i in range(len(X)):

                prediction = self.predict(X[i])
                error = y[i] - prediction
                delta =  self.sigmoid_derivative(prediction)

                self.weights += self.learning_rate * error * delta * X[i] 
                self.bias += self.learning_rate * error *  delta


if __name__ == "__main__":
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([0, 0, 0, 1])

    perceptron = Perceptron()
    perceptron.fit(X, y)

    print("Predictions:")
    for i in range(len(X)):
        print(f"Input: {X[i]} => Prediction: {perceptron.predict(X[i]):4f}")

