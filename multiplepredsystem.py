# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 23:54:55 2025

@author: saipr
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu  # to create side bars in web app
# loading saved models
diabetes_model = pickle.load(open('C:/Users/saipr/OneDrive/Desktop/classmodel.sav','rb'))
heart_model = pickle.load(open('C:/Users/saipr/OneDrive/Desktop/regmodel.sav','rb'))
parkinson_model = pickle.load(open('C:/Users/saipr/OneDrive/Desktop/svmmodel.sav','rb'))
# side bars
with st.sidebar:
    selected = option_menu('multiple Disease prediction',  # side bar title
                           
                           ['Diabetes Prediction',   # parts in side bars
                           'Heart Disease Prediction',
                           'Parkinson Disease Prediction'],
                           
                           icons = ['activity','heart','person'],  # icons for parts in side bars
                           default_index = 0)
    
if (selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('No.of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucode Levels')
    with col3:
        BloodPressure = st.text_input('BloodPressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of a person')


    dia_diag = ''
    if st.button('Diabetes Prediction result'):
        dia_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(dia_pred[0]==1):
            dia_diag = 'The person is diabetic'
        else:
            dia_diag = 'The person is not diaabetic'
    st.success(dia_diag)

if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('age of the person')
    with col2:
        sex = st.text_input('sex of the person')
    with col3:
        cp = st.text_input('cp of the person')
    with col1:
        trestbps = st.text_input('trestbps of the person')
    with col2:
        chol = st.text_input('chol of the person')
    with col3:
        fbs = st.text_input('fbs of the person')
    with col1:
        restecg = st.text_input('restecg of the person')
    with col2:
        thalach = st.text_input('thalach of the person')
    with col3:
        exang = st.text_input('exang of the person')
    with col1:
        oldpeak = st.text_input('oldpeak of the person')
    with col2:
        slope = st.text_input('slope of the person')
    with col3:
        ca = st.text_input('ca of the person')
    with col1:
        thal = st.text_input('thal of the person')


    heart_diag = ''
    if st.button('Heart Disease Prediction result'):
        heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(dia_pred[0]==1):
            heart_diag = 'The person is diabetic'
        else:
            heart_diag = 'The person is not diaabetic'
    st.success(heart_diag)
    

if (selected=='Parkinson Disease Prediction'):
    st.title('Parkinson Disease Prediction using ML')
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        name = st.text_input('name')
    with col2:
        Fo = st.text_input('MDVP:Fo(Hz)')
    with col3:
        Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col4:
        Flo = st.text_input('MDVP:Flo(Hz)')
    with col5:
        Jitter_per = st.text_input('MDVP:Jitter(%)')
    with col1:
        Jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        RAP = st.text_input('MDVP:RAP')
    with col3:
        PPQ = st.text_input('MDVP:PPQ')
    with col4:
        DDP = st.text_input('Jitter:DDP')
    with col5:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col4:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col5:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col1:
        NHR = st.text_input('NHR')
    with col2:
        HNR = st.text_input('HNR')
    with col3:
        status = st.text_input('status')
    with col4:
        RPDE = st.text_input('RPDE')
    with col5:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col4:
        PPE = st.text_input('PPE')

    parkin_diag = ''
    if st.button('Parkinson Disease Prediction result'):
        parkin_pred = parkinson_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(dia_pred[0]==1):
            parkin_diag = 'The person is diabetic'
        else:
            parkin_diag = 'The person is not diaabetic'
    st.success(parkin_diag)