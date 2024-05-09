# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:45:32 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('multiple disease prediction/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('multiple disease prediction/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('multiple disease prediction/saved models/parkinsons_model.sav', 'rb'))

Covid_19_model = pickle.load(open('Multiple_disease_Prediction_Using_ML_And_Streamlit
/multiple disease prediction/saved models/Covid_19_model.sav', 'rb'))



# cancer_model = pickle.load(open('C:/Users/HP/Desktop/multiple disease prediction/saved models/model.pkl', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Covid 19 Prediction',],
                          icons = ['activity','heart','person','heart-pulse'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('Oldpeak = ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    # code for Prediction
    heart_diagnosis = ''
    
  
  
    if st.button('Heart Disease Test Result'):
         try:
          # Convert inputs to float
             features = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),
                      float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
          
             heart_prediction = heart_disease_model.predict([features]) 
          
             if heart_prediction[0] == 1:
              heart_diagnosis = 'The person is having heart disease'
             else:
              heart_diagnosis = 'The person does not have any heart disease'
         except ValueError:
          heart_diagnosis = 'Invalid input. Please enter valid numbers.'
        
    st.success(heart_diagnosis)
    
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
       fo = st.text_input('MDVP:Fo(Hz)')
       
    with col2:
       fhi = st.text_input('MDVP:Fhi(Hz)')
       
    with col3:
       flo = st.text_input('MDVP:Flo(Hz)')
       
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
# Covid 19 Prediction Page
if (selected == 'Covid 19 Prediction'):
    
    # page title
    st.title('Covid 19 Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        bodytemperature = st.text_input('BodyTemperature')
        
    with col3:
        fatigue = st.text_input('Fatigue')
           
    with col1:
        cough = st.text_input('Cough')
        
    with col2:
        bodypain = st.text_input('Bodypain')
        
    with col3:
        sorethroat = st.text_input('SoreThroat')
        
    with col1:
        breathingDifficulty = st.text_input('BreathingDifficulty')
        
    
        
    # code for Prediction
    Covid_diagnosis = ''
    
  
  
    if st.button('Covid 19 Test Result'):
         try:
          # Convert inputs to float
             features = [float(age), float(bodytemperature), float(fatigue), float(cough), float(bodypain), float(sorethroat), float(breathingDifficulty)]
          
             Covid_19_prediction = Covid_19_model.predict([features]) 
          
             if Covid_19_prediction[0] == 1:
              Covid_diagnosis = 'The person is having Covid 19'
             else:
              Covid_diagnosis = 'The person does not have Covid 19'
         except ValueError:
          Covid_diagnosis = 'Invalid input. Please enter valid numbers.'
        
    st.success(Covid_diagnosis)
