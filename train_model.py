import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# CSV fayldan ma'lumotni o‘qish
csv_path = 'data/aviator.csv'
df = pd.read_csv(csv_path)

# X va y qiymatlarni ajratish
X = df[['k1', 'k2', 'k3']]
y = df['next'].apply(lambda x: 1 if x >= 1.80 else 0)  # 1.80x+ bo‘lsa 1, bo‘lmasa 0

# Modelni o‘qitish
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Modelni saqlash
os.makedirs('models', exist_ok=True)
with open('models/aviator_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model muvaffaqiyatli saqlandi: models/aviator_model.pkl")
