import streamlit as st
import numpy as np
import os
import pickle

# Load the pickled model
with open('customer_satisfaction/model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.markdown(
    """
<style>
section.main button {
    height: auto;
    padding: 0 2em !important;
    background-color: #0276FF !important;
}
section.main button p{
    height: auto;
    font-size: 1.5em !important;
    color: white !important;
    font-weight: bold !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.sidebar.header('Adjust the feature sliders to predict the median value')

st.header(f"Boston Housing Price Prediction tool", divider='rainbow')
st.markdown("Welcome to our interactive Boston Housing Price Prediction tool! This application is designed to make predictions about the median value of homes in various neighborhoods around Boston. By adjusting different parameters that affect housing prices, such as crime rates, the age of homes, and access to highways, you can see how these factors might influence the real estate market.")

st.subheader("How to Use the App")
st.markdown("1. **Adjust the Parameters on the Left Panel:** You will see various sliders representing different aspects of housing data such as CRIM, RM, TAX and many more")
st.markdown("2. **Click on predict button:** After you've set the parameters, simply click the 'Predict' button. The app will then use a pre-trained machine learning model to estimate the median value of a home with those parameters.")

# Creating sliders for the input features
CRIM = st.sidebar.slider('Per capita crime rate by town (CRIM)', 0.00, 100.00, 0.26)
ZN = st.sidebar.slider('Proportion of residential land zoned (ZN)', 0.0, 100.0, 0.0)
INDUS = st.sidebar.slider('Proportion of non-retail business acres (INDUS)', 0.46, 27.74, 8.56)
CHAS = st.sidebar.selectbox('Charles River dummy variable (CHAS)', [0, 1])
NOX = st.sidebar.slider('Nitric oxides concentration (NOX, parts per 10 million)', 0.38, 0.87, 0.53)
RM = st.sidebar.slider('Average number of rooms per dwelling (RM)', 3.0, 10.0, 6.20)
AGE = st.sidebar.slider('Proportion of owner-occupied units built prior to 1940 (AGE)', 2.0, 100.0, 77.7)
DIS = st.sidebar.slider('Weighted distances to five Boston employment centres (DIS)', 1.0, 15.0, 3.19)
RAD = st.sidebar.slider('Index of accessibility to radial highways (RAD)', 1, 24, 5)
TAX = st.sidebar.slider('Full-value property-tax rate per $10,000 (TAX)', 100, 800, 330)
PTRATIO = st.sidebar.slider('Pupil-teacher ratio by town (PTRATIO)', 10.0, 23.0, 19.1)
B = st.sidebar.slider('1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town (B)', 1.0, 500.0, 392.19)
LSTAT = st.sidebar.slider('% Lower status of the population (LSTAT)', 1.0, 40.0, 11.0)


# Predict button
if st.button('Predict'):
    # Create a numpy array from the input values
    input_features = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])

    st.subheader("Parameters")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="CRIM", value=f"{CRIM}")
    col2.metric(label="ZN", value=f"{ZN}")
    col3.metric(label="INDUS", value=f"{INDUS}")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="CHAS", value=f"{CHAS}")
    col2.metric(label="NOX", value=f"{NOX}")
    col3.metric(label="RM", value=f"{RM}")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="AGE", value=f"{AGE}")
    col2.metric(label="DIS", value=f"{DIS}")
    col3.metric(label="RAD", value=f"{RAD}")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="TAX", value=f"{TAX}")
    col2.metric(label="PTRATIO", value=f"{PTRATIO}")
    col3.metric(label="B", value=f"{B}")

    st.metric(label="LSTAT", value=f"{LSTAT}")
    
    # Use the loaded model to make predictions
    prediction = loaded_model.predict(input_features)
    
    # Display the prediction
    #st.subheader(":rainbow[Prediction]")
    st.markdown(f"## :rainbow[The predicted median value of owner-occupied homes is]")
    st.markdown(f"# :rainbow[${prediction[0] * 1000:,.2f}]")
