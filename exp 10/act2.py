"""
Created on Tue May 12 08:34:23 2026

@author: pradnya

"""

import streamlit as st

st.set_page_config(page_title="BMI Health Checker", page_icon="⚕️")

st.title("⚕️ BMI Health Checker App")

st.write("Enter your height and weight to check your BMI.")

# User Input
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (meters)", min_value=0.5, step=0.01)

# BMI Calculation
if st.button("Check BMI"):

    bmi = weight / (height ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("You are Healthy")
    elif 25 <= bmi < 29.9:
        st.info("You are Overweight")
    else:
        st.error("You are Obese")

    # Health Tips
    st.markdown("## Health Tips")

    if bmi < 18.5:
        st.write("• Eat nutritious food")
        st.write("• Increase protein intake")
        st.write("• Exercise regularly")
    elif 18.5 <= bmi < 24.9:
        st.write("• Maintain a balanced diet")
        st.write("• Continue regular exercise")
        st.write("• Stay hydrated")
    elif 25 <= bmi < 29.9:
        st.write("• Reduce junk food")
        st.write("• Do daily exercise")
        st.write("• Eat more fruits and vegetables")
    else:
        st.write("• Consult a doctor or nutritionist")
        st.write("• Follow a healthy diet plan")
        st.write("• Exercise daily")

st.markdown("---")
st.caption("Made with Streamlit ❤️")
