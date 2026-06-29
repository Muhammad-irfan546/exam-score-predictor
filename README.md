
# 📚 Exam Score Predictor

A Machine Learning web app that predicts student exam scores
based on study hours using Linear Regression.

## 🌐 Live Demo
👉 https://github.com/Muhammad-irfan546/exam-score-predictor

## 📊 Project Overview
- **Problem:** Predict how much a student will score based on study hours
- **Model:** Linear Regression
- **Dataset:** Student exam data (study hours vs exam score)
- **Accuracy:** R2 Score ~ 0.97

## 🛠️ Tools & Technologies
- Python
- Pandas & NumPy
- Scikit-learn (Linear Regression)
- Matplotlib & Seaborn
- Streamlit (Web UI)
- GitHub (Version Control)
- Streamlit Cloud (Deployment)

## 📁 Project Structure
```
exam-score-predictor/
│
├── app.py                    ← Streamlit web app
├── model.pkl                 ← Trained ML model
├── requirements.txt          ← Required libraries
├── student_exam_data_v1.csv  ← Dataset
└── README.md                 ← Project description
```

## 🚀 How To Run Locally
```bash
# Install libraries
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## 📈 How It Works
1. User selects study hours using a slider (0 to 10 hours)
2. App feeds input to trained Linear Regression model
3. Model predicts the exam score instantly
4. App shows score out of 100 with performance message

## 📊 Model Performance
| Metric | Score |
|--------|-------|
| R2 Score | ~0.97 |
| MAE | ~2.5 |
| RMSE | ~3.1 |

## 👨‍💻 Author
**Muhammad Irfan**
- GitHub: [@Muhammad-irfan546](https://github.com/Muhammad-irfan546)

## 📌 What I Learned
- Data cleaning and preprocessing
- Training Linear Regression model
- Model evaluation (R2, MAE, RMSE)
- Building web UI with Streamlit
- Deploying ML app on Streamlit Cloud
- Version control with Git & GitHub

