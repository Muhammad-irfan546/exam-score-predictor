import streamlit as st
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Exam Score Predictor", page_icon="📚")
st.title("📚 Exam Score Predictor")
st.markdown("Predict a student exam score based on study hours.")
st.divider()

# ✅ Green button CSS
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 30px;
        border: none;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #218838;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Slider - step 0.1 allows all values
study_hours = st.slider(
    "How many hours did the student study?",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

st.write(f"Selected Study Hours: **{study_hours}**")

# ✅ Green Predict Button
if st.button("🎯 Predict Exam Score"):
    input_data = np.array([[study_hours]])
    raw_prediction = model.predict(input_data)[0]

    # Cap between 0 and 100
    prediction = float(np.clip(raw_prediction, 0, 100))

    st.divider()
    st.success(f"📊 Predicted Exam Score: **{prediction:.1f} / 100**")
    st.progress(int(prediction))

    if prediction >= 80:
        st.info("🟢 Excellent performance expected!")
    elif prediction >= 60:
        st.info("🟡 Good performance expected.")
    elif prediction >= 40:
        st.info("🟠 Average performance - study more!")
    else:
        st.info("🔴 Needs more study hours.")

st.divider()
st.markdown("Built with Streamlit and Scikit-learn")
