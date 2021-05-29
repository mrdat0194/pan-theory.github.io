import os
import keras
import warnings
import pandas as pd
from keras import optimizers
import tensorflow as tf
from tensorflow.python.util import deprecation
from MLModel.data_pipeline import data_helper
from MLModel import DATA_DIR

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
deprecation._PRINT_DEPRECATION_WARNINGS = False

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)


def test(test_link, result_link):

    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    # Get data for predict
    X_final_test, ID = data_helper.get_data_test(test_link)

    # Model path
    model_path = '..\model_nn_save\\'

    # Load model
    json_file = open(model_path + 'model_nn.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = keras.models.model_from_json(loaded_model_json)

    # Load weights into new model
    model.load_weights(model_path + 'model_nn.h5')

    # Compile model
    # sgd = keras.optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True)
    sgd = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, amsgrad=True)
    model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])

    # Predict
    results = model.predict_classes(X_final_test)

    if os.path.exists(result_link):
        print('Result file existed :))')
    else:
        result_matrix = {'id': ID, 'label': results}

        df = pd.DataFrame(result_matrix)
        df.to_csv(result_link, index=False)


if __name__ == "__main__":

    csv_test = os.path.join(DATA_DIR, "test_encode.csv")
    result = os.path.join(DATA_DIR, "MLResult","nn","result_23_0.5_v1.csv")

    test(csv_test, result)
else:
    print("Classification is being imported into another module.")

