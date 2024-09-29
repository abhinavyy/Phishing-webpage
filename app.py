import streamlit as st
import pandas as pd
import joblib
import os

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Load the Random Forest model from the correct path
model_path = os.path.join(current_dir, 'phishing_rf_model.pkl')
model = joblib.load(model_path)

# Set the app title and layout
st.set_page_config(page_title="Phishing Website Detection", layout="wide")

# Header
st.title("🔍 Phishing Website Detection")
st.markdown("""
    This app predicts whether a given URL is phishing or legitimate based on various features.
    Please enter the details below to make a prediction.
""")

# Sidebar for input features
st.sidebar.header("Input Features")

# Input fields for the features
NumDots = st.sidebar.number_input('Number of Dots in URL', min_value=0, max_value=10, step=1)
PathLevel = st.sidebar.number_input('Path Level', min_value=0, max_value=5, step=1)
NumHash = st.sidebar.number_input('Number of Hashes in URL', min_value=0, max_value=5, step=1)
PctExtResourceUrls = st.sidebar.number_input('Percentage of External Resource URLs', min_value=0.0, max_value=100.0, step=0.1)
InsecureForms = st.sidebar.number_input('Insecure Forms', min_value=0, max_value=1, step=1)
PctNullSelfRedirectHyperlinks = st.sidebar.number_input('Percentage of Null Self Redirect Hyperlinks', min_value=0.0, max_value=100.0, step=0.1)
FrequentDomainNameMismatch = st.sidebar.number_input('Frequent Domain Name Mismatch', min_value=0, max_value=1, step=1)
SubmitInfoToEmail = st.sidebar.number_input('Submit Info To Email', min_value=0, max_value=1, step=1)
IframeOrFrame = st.sidebar.number_input('Iframe Or Frame', min_value=0, max_value=1, step=1)

# Button to make predictions
if st.sidebar.button('Predict'):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'NumDots': [NumDots],
        'PathLevel': [PathLevel],
        'NumHash': [NumHash],
        'PctExtResourceUrls': [PctExtResourceUrls],
        'InsecureForms': [InsecureForms],
        'PctNullSelfRedirectHyperlinks': [PctNullSelfRedirectHyperlinks],
        'FrequentDomainNameMismatch': [FrequentDomainNameMismatch],
        'SubmitInfoToEmail': [SubmitInfoToEmail],
        'IframeOrFrame': [IframeOrFrame]
    })

    # Predict using the model
    prediction = model.predict(input_data)

    # Display the result with an appropriate message
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.markdown("<h3 style='color: red;'>🚫 This is a phishing website!</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: green;'>✅ This is a legitimate website.</h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Phishing Detection App. All rights reserved.")
