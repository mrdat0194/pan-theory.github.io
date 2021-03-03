import os
import keras
import tensorflow as tf
from tensorflow.python.util import deprecation

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
deprecation._PRINT_DEPRECATION_WARNINGS = False

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


def model_nn(input_shape, n_classes):

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(300, input_shape=input_shape, activation='sigmoid', kernel_initializer='glorot_normal', name='dense_1'))

    model.add(keras.layers.Dense(units=n_classes, activation='sigmoid', name='output_layer'))

    sgd = keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)
    # sgd = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, amsgrad=True)

    model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])

    return model
