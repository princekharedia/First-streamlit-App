import streamlit as st

st.title("BMI Calculator")

with st.form("BMI Calculator"):
    col1,col2,col3 = st.columns([3,2,1])

with col1 :
    weight = st.number_input("Enter Your Weight in kgs")
with col2 :
    height = st.number_input("Enter Your Height in meters")    
with col3:
    submit = st.form_submit_button('Calculate')

if submit :
    BMI = round(weight / (height ** 2),2)
    if (BMI <= 18.5):
        st.error("Underweight")
    elif (BMI > 18.5 and BMI < 25):
        st.success("Normal")
    elif (BMI >= 25 and BMI < 30):
        st.warning("Overweight")
    else:
        st.error("Obese")