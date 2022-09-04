import pandas as pd
import pickle
import joblib
import warnings
warnings.filterwarnings("ignore")

with open('null_dict.pkl','rb') as f:
    null_dict = pickle.load(f)

with open('columns_list.pkl', 'rb') as f:
    columns_list = pickle.load(f)

with open('encoded_list.pkl', 'rb') as f:
    encoded_list = pickle.load(f)

std_scaler = joblib.load("std_scaler.bin")

loaded_model = pickle.load(open("application_model.sav", 'rb'))



def data_preprocessing(test_data_df):
    test_df = test_data_df[columns_list]
    for col in ["DAYS_BIRTH", "DAYS_EMPLOYED", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH"]:
        test_df[col] = test_df[col].abs()/365

    for col in columns_list:
        test_df[col] = test_df[col].fillna(null_dict[col])

    test_df = pd.get_dummies(test_df, columns=test_df.select_dtypes(include=['object']).copy().columns)
    test_encoded_list = list(test_df.columns)
    test_absent_list = []
    for column in encoded_list:
        if column not in test_encoded_list:
            test_absent_list.append(column)
            test_df[column] = 0
    test_df = test_df[encoded_list]
    test_df = std_scaler.transform(test_df)
    test_pred = loaded_model.predict(test_df)
    test_data_df["TARGET_predicted"] = list(map(lambda x: 0 if x == "Approved" else 1, test_pred))
    return test_data_df