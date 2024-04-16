import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Load the trained model
def load_model():
    return pickle.load(open('modelRF.pickle','rb'))

rfm_model = load_model()

image = Image.open("cc_fraud.webp")

# Display the image using Streamlit
st.image(image, use_column_width=True)

st.header("Credit Card Fraud Detection")
st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit application employs a Machine Learning model to identify fraudulent credit card transactions using 2 Known feautures and 15 PCA-transformed features.** 

The notebook, model and documentation are available on [GitHub.](https://github.com/dars180602/Credit-Card-Fraud-Detection)        

**Contributors:** 
- **Cecille Jatulan**
- **David Higuera**
- **Diana Reyes**
- **Mike Montanez**
- **Maria Melencio**
""")

st.subheader("Enter an input array")
input_array = st.text_input("Enter your input array (separated by commas): ")

if st.button('Make Prediction'):
    if ',' not in input_array:
        st.write("Array format should have commas.")
    else:
        temp_array = input_array.split(',')
        try:
            temp_array = np.array(temp_array, dtype=np.float32)
            rfm_pred_array = rfm_model.predict(np.array([temp_array]))
            rfm_result = "Random Forest Classifier Model predicted: "
            if rfm_pred_array[0] < 0.5:
                rfm_result += "The transaction IS NOT fraudulent"
            else:
                rfm_result += "The transaction IS fraudulent"
            
            # Get the actual prediction from the model
            actual_prediction = rfm_model.predict_proba(np.array([temp_array]))[0][1]
            st.write(rfm_result)
            st.write("Actual Prediction Probability:", actual_prediction)
        except ValueError:
            st.write("Invalid input. Please enter numerical values separated by commas.")
