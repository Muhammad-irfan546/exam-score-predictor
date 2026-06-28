import streamlit as st
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Exam Score Predictor", page_icon="📚")
st.title("📚 Exam Score Predictor")
st.markdown("Predict a student exam score based on study hours.")
st.divider()

study_hours = st.slider("How many hours did the student study?",
                        min_value=0.0, max_value=12.0,
                        value=5.0, step=0.5)

if st.button("Predict Exam Score"):
    input_data = np.array([[study_hours]])
    prediction = model.predict(input_data)[0]
    st.divider()
    st.success(f"Predicted Exam Score: {prediction:.2f} / 100")
    if prediction >= 80:
        st.info("Excellent performance expected!")
    elif prediction >= 60:
        st.info("Good performance expected.")
    else:
        st.info("Needs more study hours.")

st.divider()
st.markdown("Built with Streamlit and Scikit-learn")
