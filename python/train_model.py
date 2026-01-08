import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv("water_quality_dataset.csv")

X = df[['ph','turbidity','temp','tds']]
y = df['pollution_level']

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(random_state=42))
])

params = {
    'rf__n_estimators': [150, 200],
    'rf__max_depth': [8, 10, 12]
}

grid = GridSearchCV(pipeline, params, cv=5)
grid.fit(X, y)

joblib.dump(grid.best_estimator_, "model.pkl")
print("Best model trained and saved")
