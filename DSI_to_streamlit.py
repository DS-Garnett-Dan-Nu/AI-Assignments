import streamlit as st 
import pickle
#import joblib

# da title
st.title('Welcome to DSI Fish Weight Calculater')
st.text("Assignment 1 by DS and Hsi")

# take parameters
l1 = st.number_input("Enter your Length 1 (in cm)")
l2 = st.number_input("Enter your Length 2 (in cm)")
l3 = st.number_input("Enter your Length 3 (in cm)")
h = st.number_input("Enter your Height (in cm)")
w = st.number_input("Enter your Width (in cm)")


X_test = [[l1,l2,l3,h,w]]

#model = joblib.load("DSI_fish_model.joblib")

model = pickle.load(open("DS_FISH_MODEL.pkl",'rb'))
result = model.predict(X_test)
print(result)

# check button pressed
if(st.button('Calculate Fish Weight')):

    #fish weight yay!
    st.success("Your Fish Weight is {} g.".format(result))
