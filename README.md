❤️ Heart Disease Prediction App

A Machine Learning web application built with Streamlit that predicts the likelihood of heart disease based on user health inputs. The app uses a trained K-Nearest Neighbors (KNN) model and provides an easy-to-use interactive interface for quick predictions.

🚀 Features
Interactive and user-friendly Streamlit interface
Real-time heart disease prediction
Input patient health details using sliders and dropdowns
Uses trained KNN model for classification
Data preprocessing with saved scaler
Fast and lightweight deployment
🛠️ Tech Stack
Python
Streamlit
Pandas
Scikit-learn
Joblib
📊 Input Parameters

The model uses the following health attributes:

Age
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Maximum Heart Rate
Oldpeak
Sex
Chest Pain Type
Resting ECG
Exercise Angina
ST Slope

📁 Project Files
app.py → Main Streamlit application
KNN_HEART.pkl → Trained KNN model
scaler.pkl → Feature scaler
columns.pkl → Expected feature columns
requirements.txt → Dependencies

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

🎯 Prediction Output
Low Risk of Heart Disease ✅
High Risk of Heart Disease ⚠️

📌 Purpose
This project demonstrates how Machine Learning models can be integrated into web apps for healthcare risk prediction and educational purposes.

Built with ❤️ using Streamlit.
