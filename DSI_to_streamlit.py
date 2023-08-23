import streamlit as st 
import joblib

# da title
st.title('Welcome to DSI Fish Weight Calculater')
st.text("Assignment 1 by DS and Hsi")

# take weight and height
l1 = st.number_input("Enter your Length 1 (in cm)")
l2 = st.number_input("Enter your Length 2 (in cm)")
l3 = st.number_input("Enter your Length 3 (in cm)")
h = st.number_input("Enter your Height (in cm)")
w = st.number_input("Enter your Width (in cm)")


X_test = [[l1,l2,l3,h,w]]

model = joblib.load("DSI_fish_model.joblib")

result = model.predict(X_test)
print(result)

# check button pressed
if(st.button('Calculate Fish Weight')):

    #print BMI index 
    st.success("Your Fish Weight Index id {} g.".format(result))