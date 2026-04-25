import streamlit as st
import pandas as pd
import joblib #for unpickling

model = joblib.load(KNN_HEART.pkl)
scaler = joblib.load(KNN_HEART.pkl)
expected_columns = joblib.load(KNN_HEART.pkl)

