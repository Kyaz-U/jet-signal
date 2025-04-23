import pandas as pd
import numpy as np
import pickle
import os

def predict_signal():
    # Modelni yuklash
    model_path = 'models/aviator_model.pkl'
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # CSV fayldan oxirgi 3 ta koeffitsiyentni olish
    df = pd.read_csv('data/aviator.csv')
    last_row = df.tail(1)
    k1 = float(last_row['k1'])
    k2 = float(last_row['k2'])
    k3 = float(last_row['k3'])

    input_data = np.array([[k1, k2, k3]])
    prediction = model.predict_proba(input_data)[0][1] * 100  # 1.80x+ ehtimoli

    return round(prediction, 1), [k1, k2, k3]
