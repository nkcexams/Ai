import numpy as np
import matplotlib.pyplot as plt
import h5py
import tensorflow as tf

# Load and preprocess dataset
def load_data():
    with h5py.File('train_catvnoncat.h5', "r") as train, h5py.File('test_catvnoncat.h5', "r") as test:
        return (
            train["train_set_x"][:] / 255., train["train_set_y"][:],
            test["test_set_x"][:] / 255., test["test_set_y"][:]
        )

# Visualize sample images
def visualize_data(images, labels, num_samples=5):
    plt.figure(figsize=(10, 5))
    for i in range(num_samples):
        plt.subplot(1, num_samples, i + 1)
        plt.imshow(images[i])
        plt.title(f"Label: {labels[i]}")
        plt.axis('off')
    plt.show()

# Build and train model
def train_model(train_x, train_y, test_x, test_y):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(64, 64, 3)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(train_x, train_y, epochs=50, batch_size=32, verbose=1)
    print(f"Test accuracy: {model.evaluate(test_x, test_y)[1] * 100:.2f} %")

# Execute
train_x, train_y, test_x, test_y = load_data()
visualize_data(train_x, train_y)
train_model(train_x, train_y, test_x, test_y)

