import numpy as np

class RBFPerceptron:
    def __init__(self, n_centers, gamma=1.0, learning_rate=0.1, epochs=1000):

        self.n_centers = n_centers
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.epochs = 1000

    def rbf(self, x, c):
        return np.exp(-self.gamma * np.linalg.norm(x - c) ** 2)

    def fit(self, X, y):

        n_samples, n_features = X.shape
        self.weights = np.random.randn(self.n_centers)
        self.centers = X[np.random.choice(n_samples, self.n_centers, replace=False)]


        for epoch in range(self.epochs):
            for i in range(n_samples):

                rbf_outputs = np.array([self.rbf(X[i], c) for c in self.centers])
                output = np.dot(self.weights, rbf_outputs)

                error = y[i] - output
                if error != 0:
                    self.weights += self.learning_rate * error * rbf_outputs

    def predict(self, X):
        predictions = []
        for x in X:
            rbf_outputs = np.array([self.rbf(x, c) for c in self.centers])
            output = np.dot(self.weights, rbf_outputs)
            predictions.append(np.sign(output))
        return np.array(predictions)
    

if __name__ == "__main__":
    X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    y = np.array([-1, 1, 1, -1])

    perceptron = RBFPerceptron(n_centers=2, gamma=1.0, learning_rate=0.1, epochs=10)
    perceptron.fit(X, y)

    predictions = perceptron.predict(X)
    print("Predictions:", predictions)
