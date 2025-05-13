import streamlit as st
import pickle

st.title("Weather Prediction App.")
pn=st.number_input("Enter the precipitation")
maxt=st.number_input("Enter the maximum temperature")
mint=st.number_input("Enter the minimum temperature")
wind=st.number_input("Enter the wind speed")
button=st.button("Predict!")
if button:
     lr=pickle.load(open("wp.pkl","rb"))
     res=lr.predict([[pn,maxt,mint,wind]])[0]
     st.markdown(f"Today Weather Situation:{res}")
     




