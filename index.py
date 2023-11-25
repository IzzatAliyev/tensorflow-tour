import tensorflow as tf

print("TensorFlow version:", tf.__version__)

tensor = tf.constant("Hello, TensorFlow!")
print(tensor)

# download so lang and not efficient to build locally(better to use google colab)
mnist = tf.keras.datasets.mnist
print(mnist)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
