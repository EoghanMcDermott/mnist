import tensorflow as tf

#loading MNIST handwritten digit dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train= x_train/255.0, 
x_test = x_test/255.0
#values are between 0-255, normalise those values

#build a sequential model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)), #28x28 pixels
    tf.keras.layers.Dense(128, activation='relu'),#128 neuron layer
    tf.keras.layers.Dense(10, activation='softmax') #10 layers for values 0-9
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
#train the model

model.evaluate(x_test, y_test)
#evaluate test set on trained model
