import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train,x_test = x_train / 255.0, x_test / 255.0

#Build the model
# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),      
    layers.Dense(128),                          
    layers.LeakyReLU(alpha=0.01),               
    layers.Dense(10, activation='softmax')      
])

#compile the model
model.compile(optimizer='RMSprop'
              loss='sparse_categorical_crossentropy'
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=7)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_accuracy:.4f}")

# Make predictions
predictions = model.predict(x_test)

plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.axis('off')
plt.show()

