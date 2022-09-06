import streamlit as st
import pandas as pd
import data_preprocessing
from datetime import datetime

dp_dict = dict()
st.title("Bank Loan Application Prediction")
st.write("-An ML application that predicts whether the loan can be sanctioned or not")

pred_way = st.radio("How would you like to make predictions?", ('All at once (File Upload)', 'Predict one at a time (Manual Entry of data)'))
if pred_way == "All at once (File Upload)":
    test_file = st.file_uploader("Please upload the file to obtain results")

    if test_file is not None:
        test_file_df = pd.DataFrame()
        file_format = test_file.name.split(".")[-1]
        if (file_format == "csv" or file_format == "xls" or file_format == "xlsx"):
            if (file_format=="csv"):
                test_file_df = pd.read_csv(test_file)
            else:
                test_file_df = pd.read_excel(test_file)
            st.header("Information about the uploaded data:")
            st.write("Number of records - ", test_file_df.shape[0])
            st.write("Number of columns - ", test_file_df.shape[1])
            test_df = data_preprocessing.file_data_preprocessing(test_file_df)
            st.header("Ready to download results")
            st.write("Thank you for using the application. Click on the button below to download the results")
            st.download_button("Download Results", test_df.to_csv(index=False), file_name='Predictions_'+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'.csv', mime='text/csv')
        else:
            st.write("Only csv, xls and xlsx are acceptable formats for file upload")

else:
    st.write("Please complete the below form and click on Submit to obtain the prediction")
    cnt_children = int(st.selectbox("Select the value for CNT_CHILDREN", range(0, 20)))
    st.write("Selected value for CNT_CHILDREN: ", cnt_children)
    dp_dict["CNT_CHILDREN"] = cnt_children

    amt_income_total = st.text_input('Enter the value for AMT_INCOME_TOTAL')
    if amt_income_total:
        st.write('Entered value for AMT_INCOME_TOTAL: ', amt_income_total)
        dp_dict["AMT_INCOME_TOTAL"] = float(amt_income_total)

    amt_credit = st.text_input('Enter the value for AMT_CREDIT')
    if amt_credit:
        st.write('Entered value for AMT_CREDIT: ', amt_credit)
        dp_dict["AMT_CREDIT"] = float(amt_credit)

    region_population_relative = st.text_input('Enter the value for REGION_POPULATION_RELATIVE')
    if region_population_relative:
        st.write('Entered value for REGION_POPULATION_RELATIVE: ', region_population_relative)
        dp_dict["REGION_POPULATION_RELATIVE"] = float(region_population_relative)

    days_birth = st.text_input('Enter the value for DAYS_BIRTH')
    if days_birth:
        st.write('Entered value for DAYS_BIRTH: ', days_birth)
        dp_dict["DAYS_BIRTH"] = abs(int(days_birth))/365

    days_employed = st.text_input('Enter the value for DAYS_EMPLOYED')
    if days_employed:
        st.write('Entered value for DAYS_EMPLOYED: ', days_employed)
        dp_dict["DAYS_EMPLOYED"] = abs(int(days_employed))/365

    days_registration = st.text_input('Enter the value for DAYS_REGISTRATION')
    if days_registration:
        st.write('Entered value for DAYS_REGISTRATION: ', days_registration)
        dp_dict["DAYS_REGISTRATION"] = abs(int(days_registration))/365

    days_id_publish = st.text_input('Enter the value for DAYS_ID_PUBLISH')
    if days_id_publish:
        st.write('Entered value for DAYS_ID_PUBLISH: ', days_id_publish)
        dp_dict["DAYS_ID_PUBLISH"] = abs(int(days_id_publish))/365

    hour_appr_process_start = int(st.selectbox('Select the value for HOUR_APPR_PROCESS_START', range(0, 24)))
    st.write('Selected value for HOUR_APPR_PROCESS_START: ', hour_appr_process_start)
    dp_dict["HOUR_APPR_PROCESS_START"] = hour_appr_process_start

    reg_region_not_live_region = int(st.selectbox('Select the value for REG_REGION_NOT_LIVE_REGION', [0, 1]))
    st.write('Selected value for REG_REGION_NOT_LIVE_REGION: ', reg_region_not_live_region)
    dp_dict["REG_REGION_NOT_LIVE_REGION"] = reg_region_not_live_region

    reg_city_not_live_city = int(st.selectbox('Select the value for REG_CITY_NOT_LIVE_CITY', [0, 1]))
    st.write('Selected value for REG_CITY_NOT_LIVE_CITY: ', reg_city_not_live_city)
    dp_dict["REG_CITY_NOT_LIVE_CITY"] = reg_city_not_live_city

    reg_city_not_work_city = int(st.selectbox('Select the value for REG_CITY_NOT_WORK_CITY', [0, 1]))
    st.write('Selected value for REG_CITY_NOT_WORK_CITY: ', reg_city_not_work_city)
    dp_dict["REG_CITY_NOT_WORK_CITY"] = reg_city_not_work_city

    ext_source_2 = st.text_input('Enter the value for EXT_SOURCE_2')
    if ext_source_2:
        st.write('Entered value for EXT_SOURCE_2: ', ext_source_2)
        dp_dict["EXT_SOURCE_2"] = abs(float(ext_source_2))

    ext_source_3 = st.text_input('Enter the value for EXT_SOURCE_3')
    if ext_source_3:
        st.write('Entered value for EXT_SOURCE_3: ', ext_source_3)
        dp_dict["EXT_SOURCE_3"] = abs(float(ext_source_3))

    obs_30_cnt_social_circle = st.text_input('Enter the value for OBS_30_CNT_SOCIAL_CIRCLE')
    if obs_30_cnt_social_circle:
        st.write('Entered value for OBS_30_CNT_SOCIAL_CIRCLE: ', obs_30_cnt_social_circle)
        dp_dict["OBS_30_CNT_SOCIAL_CIRCLE"] = abs(float(obs_30_cnt_social_circle))

    def_30_cnt_social_circle = st.text_input('Enter the value for DEF_30_CNT_SOCIAL_CIRCLE')
    if def_30_cnt_social_circle:
        st.write('Entered value for DEF_30_CNT_SOCIAL_CIRCLE: ', def_30_cnt_social_circle)
        dp_dict["DEF_30_CNT_SOCIAL_CIRCLE"] = abs(float(def_30_cnt_social_circle))

    amt_req_credit_bureau_week = st.text_input('Enter the value for AMT_REQ_CREDIT_BUREAU_WEEK')
    if amt_req_credit_bureau_week:
        st.write('Entered value for AMT_REQ_CREDIT_BUREAU_WEEK: ', amt_req_credit_bureau_week)
        dp_dict["AMT_REQ_CREDIT_BUREAU_WEEK"] = abs(float(amt_req_credit_bureau_week))

    amt_req_credit_bureau_mon = st.text_input('Enter the value for AMT_REQ_CREDIT_BUREAU_MON')
    if amt_req_credit_bureau_mon:
        st.write('Entered value for AMT_REQ_CREDIT_BUREAU_MON: ', amt_req_credit_bureau_mon)
        dp_dict["AMT_REQ_CREDIT_BUREAU_MON"] = abs(float(amt_req_credit_bureau_mon))

    amt_req_credit_bureau_qrt = st.text_input('Enter the value for AMT_REQ_CREDIT_BUREAU_QRT')
    if amt_req_credit_bureau_qrt:
        st.write('Entered value for AMT_REQ_CREDIT_BUREAU_QRT: ', amt_req_credit_bureau_qrt)
        dp_dict["AMT_REQ_CREDIT_BUREAU_QRT"] = abs(float(amt_req_credit_bureau_qrt))

    amt_req_credit_bureau_year = st.text_input('Enter the value for AMT_REQ_CREDIT_BUREAU_YEAR')
    if amt_req_credit_bureau_year:
        st.write('Entered value for AMT_REQ_CREDIT_BUREAU_YEAR: ', amt_req_credit_bureau_year)
        dp_dict["AMT_REQ_CREDIT_BUREAU_YEAR"] = abs(float(amt_req_credit_bureau_year))

    name_contract_type = str(st.selectbox('Select the value for NAME_CONTRACT_TYPE', ["Cash loans", "Revolving loans"]))
    st.write('Selected value for NAME_CONTRACT_TYPE: ', name_contract_type)
    dp_dict["NAME_CONTRACT_TYPE"] = name_contract_type

    code_gender = str(st.selectbox('Select the value for CODE_GENDER', ["M", "F"]))
    st.write('Selected value for CODE_GENDER: ', code_gender)
    dp_dict["CODE_GENDER"] = code_gender

    flag_own_car = str(st.selectbox('Select the value for FLAG_OWN_CAR', ["N", "Y"]))
    st.write('Selected value for FLAG_OWN_CAR: ', flag_own_car)
    dp_dict["FLAG_OWN_CAR"] = flag_own_car

    flag_own_realty = str(st.selectbox('Select the value for FLAG_OWN_REALTY', ["N", "Y"]))
    st.write('Selected value for FLAG_OWN_REALTY: ', flag_own_realty)
    dp_dict["FLAG_OWN_REALTY"] = flag_own_realty

    name_type_suite = str(st.selectbox('Select the value for NAME_TYPE_SUITE', ["Unaccompanied", "Family", "Spouse, partner", "Children", "Other_A", "Other_B", "Group of people"]))
    st.write('Selected value for NAME_TYPE_SUITE: ', name_type_suite)
    dp_dict["NAME_TYPE_SUITE"] = name_type_suite

    name_income_type = str(st.selectbox('Select the value for NAME_INCOME_TYPE', ['Working', 'State servant', 'Commercial associate', 'Pensioner', 'Student', 'Businessman', 'Maternity leave']))
    st.write('Selected value for NAME_INCOME_TYPE: ', name_income_type)
    dp_dict["NAME_INCOME_TYPE"] = name_income_type

    name_education_type = str(st.selectbox('Select the value for NAME_EDUCATION_TYPE', ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree']))
    st.write('Selected value for NAME_EDUCATION_TYPE: ', name_education_type)
    dp_dict["NAME_EDUCATION_TYPE"] = name_education_type

    name_family_status = str(st.selectbox('Select the value for NAME_FAMILY_STATUS', ['Single / not married', 'Married', 'Civil marriage', 'Widow', 'Separated', 'Unknown']))
    st.write('Selected value for NAME_FAMILY_STATUS: ', name_family_status)
    dp_dict["NAME_FAMILY_STATUS"] = name_family_status

    name_housing_type = str(st.selectbox('Select the value for NAME_HOUSING_TYPE', ['House / apartment', 'Rented apartment', 'With parents', 'Municipal apartment', 'Office apartment', 'Co-op apartment']))
    st.write('Selected value for NAME_HOUSING_TYPE: ', name_housing_type)
    dp_dict["NAME_HOUSING_TYPE"] = name_housing_type

    weekday_appr_process_start = str(st.selectbox('Select the value for WEEKDAY_APPR_PROCESS_START', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']))
    st.write('Selected value for WEEKDAY_APPR_PROCESS_START: ', weekday_appr_process_start)
    dp_dict["WEEKDAY_APPR_PROCESS_START"] = weekday_appr_process_start

    organization_type_list = ['Advertising', 'Agriculture', 'Bank', 'Business Entity Type 1', 'Business Entity Type 2',
                              'Business Entity Type 3', 'Cleaning', 'Construction', 'Culture', 'Electricity',
                              'Emergency', 'Government', 'Hotel', 'Housing', 'Industry: type 1', 'Industry: type 10',
                              'Industry: type 11', 'Industry: type 12', 'Industry: type 13', 'Industry: type 2',
                              'Industry: type 3', 'Industry: type 4', 'Industry: type 5', 'Industry: type 6',
                              'Industry: type 7', 'Industry: type 8', 'Industry: type 9', 'Insurance', 'Kindergarten',
                              'Legal Services', 'Medicine', 'Military', 'Mobile', 'Other', 'Police', 'Postal',
                              'Realtor', 'Religion', 'Restaurant', 'School', 'Security', 'Security Ministries',
                              'Self-employed', 'Services', 'Telecom', 'Trade: type 1', 'Trade: type 2', 'Trade: type 3',
                              'Trade: type 4', 'Trade: type 5', 'Trade: type 6', 'Trade: type 7', 'Transport: type 1',
                              'Transport: type 2', 'Transport: type 3', 'Transport: type 4', 'University']
    organization_type = str(st.selectbox('Enter the value for ORGANIZATION_TYPE', organization_type_list))
    st.write('Selected value for ORGANIZATION_TYPE: ', organization_type)
    dp_dict["ORGANIZATION_TYPE"] = organization_type

    if st.button("Predict the outcome"):
        pred = data_preprocessing.dp_preprocessing(dp_dict)
        if pred == "Not Approved":
            st.write("Predicted Output: TARGET = 1. Hence ", pred)
        else:
            st.write("Predicted Output: TARGET = 0. Hence ", pred)
    else:
        st.write("Click on the above button to obtain results")



