import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Plot Activation Functions
x = np.linspace(-10, 10, 400)
plt.figure(figsize=(8, 5))
plt.plot(x, np.maximum(0, x), label="ReLU")
plt.plot(x, 1 / (1 + np.exp(-x)), label="Sigmoid")
plt.plot(x, np.tanh(x), label="Tanh")
plt.legend()
plt.title("Activation Functions")
plt.grid()
plt.show()

# Load dataset
X, y = loadtxt('pima.csv', delimiter=',')[:, :-1], loadtxt('prac7b.csv', delimiter=',')[:, -1]

# Define and train model
model = Sequential([
    Dense(12, activation='relu', input_shape=(X.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=150, batch_size=10, verbose=0)

# Evaluate model
print(f'Accuracy: {model.evaluate(X, y, verbose=0)[1]:.2%}')

# Predictions
preds = (model.predict(X[:5]) > 0.5).astype(int).flatten()
for i, p in enumerate(preds):
    print(f'Input: {X[i].tolist()} => Predicted: {p}, Expected: {int(y[i])}')


