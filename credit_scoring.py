import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('credit_score_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Predict Your Credit Score!')

# Input
num_bank_accounts = st.number_input('Total bank accounts', min_value=0, value=0)
num_credit_card = st.number_input('Total credit cards', min_value=0, value=0)
num_of_loan = st.number_input('Total loans', min_value=0, value=0)
num_delayed_payment = st.number_input('Average total delayed payments', min_value=0, max_value=100, value=0)
delay_from_due_date = st.number_input('Average days delayed from due date', min_value=0, max_value=100, value=0)
outstanding_debt = st.number_input('Outstanding debt (USD)', min_value=0, value=0)
credit_utilization_ratio = st.number_input('Credit utilization ratio (%)', min_value=1, max_value=100)
credit_history_age = st.number_input('Length of credit (Months)', min_value=0, value=0)
payment_min_amount = st.selectbox('Do you only paid the minimum amount?', ['No', 'Yes'])
payment_min_amount = 1 if payment_min_amount == 'Yes' else 0
monthly_balance = st.number_input('Monthly balance (USD)', min_value=0, value=0)

# Predict
if st.button('Predict'):
    # Input data
    input_data = pd.DataFrame([[num_bank_accounts, num_credit_card, num_of_loan, delay_from_due_date,
                                num_delayed_payment, outstanding_debt, credit_utilization_ratio,
                                credit_history_age, payment_min_amount, monthly_balance]],
                              columns=['Num_Bank_Accounts', 'Num_Credit_Card', 'Num_of_Loan',
                                       'Delay_from_due_date', 'Num_of_Delayed_Payment', 
                                       'Outstanding_Debt', 'Credit_Utilization_Ratio',
                                       'Credit_History_Age', 'Payment_of_Min_Amount', 'Monthly_Balance'])
    
    # Predict the credit score
    credit_score_prediction = model.predict(input_data)
    
    st.write(f'Predicted Credit Score: {credit_score_prediction[0]:.2f}')