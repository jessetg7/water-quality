import pandas as pd, joblib
from sklearn.metrics import classification_report

df = pd.read_csv("water_quality_dataset.csv")
X = df[['ph','turbidity','temp','tds']]
y = df['pollution_level']

model = joblib.load("model.pkl")
print(classification_report(y, model.predict(X)))
