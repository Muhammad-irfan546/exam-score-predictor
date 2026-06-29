import streamlit as st
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="Exam Score Predictor",
    page_icon="📚",
    layout="centered"
)

# ✅ Full Colorful CSS Design
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    }

    /* Title */
    h1 {
        color: #e94560 !important;
        text-align: center;
        font-size: 3rem !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 10px rgba(233,69,96,0.5);
        padding: 20px 0;
    }

    /* Subtitle */
    p {
        color: #a8dadc !important;
        text-align: center;
        font-size: 1.1rem !important;
    }

    /* Slider label */
    .stSlider label {
        color: #e94560 !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }

    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #e94560, #f5a623) !important;
    }

    /* Predict Button */
    div.stButton > button {
        background: linear-gradient(90deg, #e94560, #f5a623);
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        border: none !important;
        width: 100% !important;
        margin-top: 20px !important;
        box-shadow: 0px 5px 20px rgba(233,69,96,0.5) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0px 8px 25px rgba(233,69,96,0.8) !important;
    }

    /* Success box */
    .stSuccess {
        background: linear-gradient(90deg, #11998e, #38ef7d) !important;
        border-radius: 15px !important;
        padding: 20px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
        color: white !important;
    }

    /* Info box */
    .stInfo {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 1.1rem !important;
        text-align: center !important;
    }

    /* Divider */
    hr {
        border-color: #e94560 !important;
        border-width: 2px !important;
    }

    /* Selected hours text */
    .stMarkdown p {
        color: #f5a623 !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────
st.markdown("<h1>📚 Exam Score Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p>Predict student exam score based on study hours using AI</p>",
            unsafe_allow_html=True)
st.divider()

# ─── Stats Row ─────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div style='background:rgba(233,69,96,0.2); 
        border-radius:15px; padding:15px; text-align:center;
        border: 1px solid #e94560'>
        <h3 style='color:#e94560; margin:0'>🤖</h3>
        <p style='color:white; margin:0; font-size:0.9rem'>Linear Regression</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style='background:rgba(245,166,35,0.2); 
        border-radius:15px; padding:15px; text-align:center;
        border: 1px solid #f5a623'>
        <h3 style='color:#f5a623; margin:0'>📈</h3>
        <p style='color:white; margin:0; font-size:0.9rem'>R2 Score ~0.97</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div style='background:rgba(56,239,125,0.2); 
        border-radius:15px; padding:15px; text-align:center;
        border: 1px solid #38ef7d'>
        <h3 style='color:#38ef7d; margin:0'>🎯</h3>
        <p style='color:white; margin:0; font-size:0.9rem'>High Accuracy</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# ─── Slider ────────────────────────────────
study_hours = st.slider(
    "⏰ How many hours did the student study?",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

st.markdown(f"<p>⏱️ Selected Study Hours: {study_hours}</p>",
            unsafe_allow_html=True)

# ─── Predict Button ────────────────────────
if st.button("🚀 Predict Exam Score"):
    input_data = np.array([[study_hours]])
    raw_prediction = model.predict(input_data)[0]
    prediction = float(np.clip(raw_prediction, 0, 100))

    st.divider()

    # Score display
    st.success(f"📊 Predicted Exam Score: {prediction:.1f} / 100")
    st.progress(int(prediction))

    # Color coded result
    if prediction >= 80:
        st.markdown("""
            <div style='background:linear-gradient(90deg,#11998e,#38ef7d);
            border-radius:15px; padding:20px; text-align:center; margin-top:10px'>
            <h2 style='color:white; margin:0'>🏆 EXCELLENT!</h2>
            <p style='color:white; margin:0'>Outstanding performance expected!</p>
            </div>
        """, unsafe_allow_html=True)
    elif prediction >= 60:
        st.markdown("""
            <div style='background:linear-gradient(90deg,#f7971e,#ffd200);
            border-radius:15px; padding:20px; text-align:center; margin-top:10px'>
            <h2 style='color:white; margin:0'>👍 GOOD!</h2>
            <p style='color:white; margin:0'>Good performance expected!</p>
            </div>
        """, unsafe_allow_html=True)
    elif prediction >= 40:
        st.markdown("""
            <div style='background:linear-gradient(90deg,#f953c6,#b91d73);
            border-radius:15px; padding:20px; text-align:center; margin-top:10px'>
            <h2 style='color:white; margin:0'>📖 AVERAGE</h2>
            <p style='color:white; margin:0'>Need to study more!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='background:linear-gradient(90deg,#e94560,#c0392b);
            border-radius:15px; padding:20px; text-align:center; margin-top:10px'>
            <h2 style='color:white; margin:0'>⚠️ NEEDS WORK!</h2>
            <p style='color:white; margin:0'>Please study more hours!</p>
            </div>
        """, unsafe_allow_html=True)

# ─── Footer ────────────────────────────────
st.divider()
st.markdown("""
    <div style='text-align:center'>
    <p style='color:#a8dadc'>Built with ❤️ by 
    <span style='color:#e94560; font-weight:bold'>Muhammad Irfan</span>
    using Streamlit & Scikit-learn</p>
    </div>
""", unsafe_allow_html=True)
