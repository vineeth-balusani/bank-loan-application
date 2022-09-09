# bank-loan-application
ML System which predicts whether the bank loan can be sanctioned or not to an applicant

This repository consists of the code for hosting the web application using Streamlit on Heroku Cloud.

The Procfile and setup.sh are the ones need to be included while hosting the application on Heroku Cloud.
requirements.txt consists of all the packages which are required for the web app to run properly.

The bank_loan_application.py has the code for launching the web application using Streamlit, whereas the data-preprocessing.py file consists of the modules for data preprocessing

The columns_list, encoded_list, null_dict pkl files and std_scaler.bin  are generated from the train data and will be used during predictions made on the test data.

The application_model.sav is the saved model which performed best on the train data.

![image](https://user-images.githubusercontent.com/15002537/189453000-43781c9b-5f21-4764-8e5a-5aabd61cd16a.png)


# Instructions to Launch the app locally
1) Clone the repository
2) Create a new virtual environment and activate the created virtual environment
3) Now execute the following command from Terminal

a) pip install -r requirements.txt
b) streamlit run bank_loan_application.py

This will host the web application locally.

# Instructions to Launch the app on Heroku
You can fork the repository and then login into Heroku.
Now, create a new app and then connect the app with GitHub repository which you have forked and then click on Deploy.
Once deployed the dynos will execute the Procfile which has instructions to host the web application 

This will host the web application on Heroku.

The application which I have deployed - https://bank-loan-application-predict.herokuapp.com/ 


