from MLModel.data_pipeline import data_helper
from MLModel.model import ada_boost
import pandas as pd
import warnings
import os
from sklearn.exceptions import DataConversionWarning
from sklearn.exceptions import UndefinedMetricWarning
from MLModel import DATA_DIR


warnings.filterwarnings(action='ignore', category=DataConversionWarning)
warnings.filterwarnings(action='ignore', category=UndefinedMetricWarning)


def run(train_link, test_link, result_link, aug_link_1, aug_link_2, save_result=0):

    X, Y = data_helper.get_data(train_link)

    X_aug_1, Y_aug_1 = data_helper.get_data(aug_link_1)

    X_aug_2, Y_aug_2 = data_helper.get_data(aug_link_2)

    X_final, Y_final = data_helper.imbalance_solve(X, Y, X_aug_1, Y_aug_1, X_aug_2, Y_aug_2, -1, 0.5)

    X_train, X_test, Y_train, Y_test = data_helper.data_pipeline(X_final, Y_final)

    ada_model = ada_boost.model_ada(X_train, X_test, Y_train, Y_test)

    X_final_test, ID = data_helper.get_data_test(test_link)
    # X_final_test = fit.transform(X_final_test)
    Y_predicted = ada_boost.ada_call(X_final_test, ada_model)
    print(Y_predicted)

    if save_result == 1:

        if os.path.exists(result_link):
            print('Result file existed :))')
        else:
            result_matrix = {'id': ID, 'label': Y_predicted}

            df = pd.DataFrame(result_matrix)
            df.to_csv(result_link, index=False)


if __name__ == "__main__":
    csv_train = os.path.join(DATA_DIR,"v1", "train_encode.csv")
    csv_test = os.path.join(DATA_DIR,"v1", "test_encode.csv")
    csv_augment_1 = os.path.join(DATA_DIR,"v1", "train_encode_age2_1.csv")
    csv_augment_2 = os.path.join(DATA_DIR,"v1", "train_encode_agemean_1.csv")

    result = os.path.join(DATA_DIR, "MLResult","ada","result_adaboost_2.csv")
    run(csv_train, csv_test, result, csv_augment_1, csv_augment_2, save_result=1)
