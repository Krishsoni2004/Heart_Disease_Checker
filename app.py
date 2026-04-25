import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

model = joblib.load("KNN_HEART.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
h1 {
    color: #d63384;
}
.stButton>button {
    width: 100%;
    background-color: #dc3545;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("heart.png.jpg", width=220)

with col2:
    st.title("❤️ Heart Disease Prediction App")
    st.write("AI powered medical screening system.")

st.sidebar.image("doctor.png", use_container_width=True)
st.sidebar.header("Health Tips")
st.sidebar.success("✔ Exercise Daily")
st.sidebar.success("✔ Healthy Diet")
st.sidebar.success("✔ Avoid Smoking")
st.sidebar.success("✔ Regular Checkup")

with st.form("heart_form"):

    st.subheader("Enter Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 20, 90, 45)
        resting_bp = st.slider("Resting BP", 80, 200, 120)
        cholesterol = st.slider("Cholesterol", 100, 600, 200)
        fasting_bs = st.selectbox("Fasting BS >120", [0, 1])
        max_hr = st.slider("Max Heart Rate", 60, 220, 150)

    with col2:
        oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
        sex = st.selectbox("Sex", ["Male", "Female"])
        chest_pain = st.selectbox("Chest Pain", ["ATA", "NAP", "TA", "ASY"])
        ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
        exercise_angina = st.selectbox("Exercise Angina", ["Yes", "No"])

    slope = st.selectbox("ST Slope", ["Flat", "Up", "Down"])

    submit = st.form_submit_button("Predict Now")

if submit:

    data = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_M": 1 if sex == "Male" else 0,
        "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain == "TA" else 0,
        "RestingECG_Normal": 1 if ecg == "Normal" else 0,
        "RestingECG_ST": 1 if ecg == "ST" else 0,
        "ExerciseAngina_Y": 1 if exercise_angina == "Yes" else 0,
        "ST_Slope_Flat": 1 if slope == "Flat" else 0,
        "ST_Slope_Up": 1 if slope == "Up" else 0
    }

    input_df = pd.DataFrame([data])
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)
    input_df = input_df.astype(float)

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
        st.image("warning.jpg", width=300)
    else:
        st.success("✅ Low Risk of Heart Disease")
        st.image("healthy.jpg", width=300)