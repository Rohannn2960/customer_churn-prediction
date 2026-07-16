import pandas as pd
import streamlit as st                      
import joblib
model = joblib.load('models/customer_churn_model.pkl')
st.title('Customer Churn Prediction')
st.write('This app predicts whether a customer will churn or not based on their features.')
st.write('Please enter the customer features below:')
tenure = st.number_input('Tenure (in months)', min_value=0, max_value=100, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, max_value=1000.0, value=70.0)   
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
gender = st.selectbox('Gender', ['Male', 'female'])
senior_citizen = st.number_input('Senior Citizen', min_value=0, max_value=1, value=0)
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
total_charges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=800.0)

input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})


st.write(input_data.columns)
st.write(model.feature_names_in_)

if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error('The customer is likely to churn.')
    else:
        st.success('The customer is not likely to churn.')