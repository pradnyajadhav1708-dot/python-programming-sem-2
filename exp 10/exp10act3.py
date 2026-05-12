# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:44:51 2026

@author: pradnya
"""

import streamlit as st

st.set_page_config(page_title="Student Result Calculator", page_icon="📚")

st.title("📚 Student Result Calculator")

st.write("Enter marks for 5 subjects")

# Input Marks
sub1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
sub2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
sub3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)
sub4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100)
sub5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100)

# Calculate Result
if st.button("Calculate Result"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    st.subheader(f"Total Marks: {total}/500")
    st.subheader(f"Percentage: {percentage:.2f}%")

    # Grade
    if percentage >= 90:
        grade = "A+"
        result = "Excellent"
    elif percentage >= 75:
        grade = "A"
        result = "Very Good"
    elif percentage >= 60:
        grade = "B"
        result = "Good"
    elif percentage >= 40:
        grade = "C"
        result = "Pass"
    else:
        grade = "F"
        result = "Fail"

    st.success(f"Grade: {grade}")
    st.info(f"Result: {result}")

st.markdown("---")
st.caption("Made with Streamlit ❤️")