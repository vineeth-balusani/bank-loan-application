import pandas as pd
import pickle
import joblib
import warnings

warnings.filterwarnings("ignore")

with open('null_dict.pkl', 'rb') as f:
    null_dict = pickle.load(f)

with open('columns_list.pkl', 'rb') as f:
    columns_list = pickle.load(f)

with open('encoded_list.pkl', 'rb') as f:
    encoded_list = pickle.load(f)

std_scaler = joblib.load("std_scaler.bin")

loaded_model = pickle.load(open("application_model.sav", 'rb'))


def file_data_preprocessing(test_data_df):
    test_df = test_data_df[columns_list]
    for col in ["DAYS_BIRTH", "DAYS_EMPLOYED", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH"]:
        test_df[col] = test_df[col].abs() / 365

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


def dp_preprocessing(dp_dict_old):
    dp_dict = dict()
    for col in list(null_dict.keys()):
        if col not in list(dp_dict_old.keys()):
            dp_dict_old[col] = null_dict[col]
    dict_not_req_keys = ["NAME_CONTRACT_TYPE", "CODE_GENDER", "FLAG_OWN_CAR", "FLAG_OWN_REALTY", "NAME_TYPE_SUITE",
                         "NAME_INCOME_TYPE", "NAME_EDUCATION_TYPE", "NAME_FAMILY_STATUS", "NAME_HOUSING_TYPE",
                         "WEEKDAY_APPR_PROCESS_START", "ORGANIZATION_TYPE"]
    dict_req_keys = list(set(dp_dict_old.keys()) - set(dict_not_req_keys))
    for cols in dict_req_keys:
        dp_dict[cols] = dp_dict_old[cols]
    for cols in dict_not_req_keys:
        dp_dict[cols+"_"+dp_dict_old[cols]] = 1
    for column in encoded_list:
        if column not in list(dp_dict.keys()):
            dp_dict[column] = 0
    dp_df = pd.DataFrame(dp_dict, index=[0])
    dp_df = dp_df[encoded_list]
    test_df = std_scaler.transform(dp_df)
    test_pred = loaded_model.predict(test_df)
    return test_pred[0]
