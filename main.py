import streamlit as st
import pickle

model = pickle.load(open("loan.pkl", "rb"))


st.title("Loan Prediction System")

income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
credit_history = st.number_input("Credit History")

if st.button("Predict"):
    prediction = model.predict([[income, loan_amount, loan_term, credit_history]])

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")



        