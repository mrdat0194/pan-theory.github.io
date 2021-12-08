import os
import warnings
import matplotlib.pyplot as plt
from MLModel.data_pipeline import data_helper
from MLModel.model import neural_network
from sklearn.exceptions import DataConversionWarning
from sklearn.exceptions import UndefinedMetricWarning
from MLModel import DATA_DIR

warnings.filterwarnings(action='ignore', category=DataConversionWarning)
warnings.filterwarnings(action='ignore', category=UndefinedMetricWarning)


def run(train_link, aug_link_1, aug_link_2):

    print('')

    X, Y = data_helper.get_data(train_link)

    X_aug_1, Y_aug_1 = data_helper.get_data(aug_link_1)

    X_aug_2, Y_aug_2 = data_helper.get_data(aug_link_2)

    X_final, Y_final = data_helper.imbalance_solve(X, Y, X_aug_1, Y_aug_1, X_aug_2, Y_aug_2, -1, 0.5)

    X_final, Y_final = data_helper.remove_duplicate(X_final, Y_final)

    X_train, X_test, X_val, Y_train, Y_test, Y_val = data_helper.data_pipeline_nn(X_final, Y_final)

    model = neural_network.model_nn((55, ), 2)

    history = model.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=64, batch_size=32, verbose=1)

    results = model.evaluate(X_test, Y_test, batch_size=32)

    save_model = '..\model_nn_save\\'
    weight_model = save_model + 'model_nn.h51'
    name_model = save_model + 'model_nn.json1'

    # Save model
    print('')
    print('Result [loss, accuracy]:', results)
    model_json = model.to_json()
    with open(name_model, "w") as json_file:
        json_file.write(model_json)

    # Save weight
    model.save_weights(weight_model)
    print('')
    print('Saved model to disk')

    # # Plot training & validation accuracy values
    # plt.figure(figsize=(19, 9))
    # plt.subplot(1, 2, 1)
    # plt.plot(history.history['acc'])
    # plt.plot(history.history['val_acc'])
    # plt.title('Model accuracy')
    # plt.ylabel('Accuracy')
    # plt.xlabel('Epoch')
    # plt.legend(['Train', 'Test'], loc='upper left')
    #
    # # Plot training & validation loss values
    # plt.subplot(1, 2, 2)
    # plt.plot(history.history['loss'])
    # plt.plot(history.history['val_loss'])
    # plt.title('Model loss')
    # plt.ylabel('Loss')
    # plt.xlabel('Epoch')
    # plt.legend(['Train', 'Test'], loc='upper left')
    #
    # plt.tight_layout()
    # plt.savefig(save_model + 'training_result_lr0.0001.png')
    # plt.close()


if __name__ == "__main__":
    csv_train = os.path.join(DATA_DIR, "train_encode.csv")
    csv_test = os.path.join(DATA_DIR, "test_encode.csv")
    csv_augment_1 = os.path.join(DATA_DIR, "train_encode_age2_1.csv")
    csv_augment_2 = os.path.join(DATA_DIR, "train_encode_agemean_1.csv")

    run(csv_train, csv_augment_1, csv_augment_2)
