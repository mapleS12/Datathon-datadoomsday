# File: modules/modeling.py
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import pandas as pd
import numpy as np


def run_modeling(inform, emdat):
    # Moving average prediction
    forecast = emdat.groupby(['year', 'country']).size().unstack(fill_value=0)
    forecast_ma = forecast.rolling(window=3).mean().iloc[-1]
    print("Forecast 2025 (3-Year MA):")
    print(forecast_ma.sort_values(ascending=False).head(3))

    # Feature importance
    disaster_freq = emdat.groupby('country').size().reset_index(name='disaster_count')
    df = inform.merge(disaster_freq, on='country', how='left').fillna(0)

    X = df.drop(columns=['country', 'disaster_count'])
    y = df['disaster_count'] > df['disaster_count'].median()

    rf = RandomForestClassifier().fit(X, y)
    importances = pd.Series(rf.feature_importances_, index=X.columns)
    print("Top 5 Predictive INFORM Indicators:")
    print(importances.sort_values(ascending=False).head(5))

