import streamlit as st
import pandas as pd

st.title('BMI Calculator')

heigth = st.slider("Enter your height (in cm):", 100, 250, 175)
weigth = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weigth / ((heigth / 100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("#### BMI Categories ###")
st.write("1. Underweight: BMI < 18.5")
st.write("2. Normal weight: BMI 18.5–24.9")
st.write("3. Overweight: BMI 25–29.9")
st.write("4. Obesity: BMI ≥ 30")