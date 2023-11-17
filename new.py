import numpy as np
import streamlit as st
import pickle

st.set_page_config(page_title="Diabetes_prediction",layout="wide")

st.title("Diabetes Prediction")

st.header("By sachidananda")

st.write("---")

#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age

model=pickle.load(open('D:/data/diabetes.pkl','rb'))


def prediction(input):
    
    output=model.predict(input)
    
    if output[0] == 1:
        return "Person Suffer from diabetes."
    else:
        return "Person not suffer from diabetes."
    
preg=st.number_input("Pregnancies")
glu=st.number_input("Glucose level")
bp =st.number_input("Blood Pressure")
sts=st.number_input("Skin Thickness") 
ins=st.number_input("Insulin")
bmi =st.number_input("BMI")
dpf=st.number_input("Diabetes Pedigree Function")
age =st.number_input("Age")


input_info=[[preg,glu,bp,sts,ins,bmi,dpf,age]]

diagnosis=''

if st.button("Prediction"):
    
    diagnosis=prediction(input_info)
    st.success(diagnosis)