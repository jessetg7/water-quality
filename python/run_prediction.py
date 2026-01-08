import requests, time, joblib, pandas as pd

model = joblib.load("model.pkl")
URL = "http://192.168.4.1/data"

while True:
    d = requests.get(URL).json()

    X = pd.DataFrame([[d['ph'], d['turbidity'], d['temperature'], d['tds']]],
                     columns=['ph','turbidity','temp','tds'])

    pred = model.predict(X)[0]

    msg = ["SAFE", "MODERATE RISK", "HIGH RISK"]
    print("Prediction:", msg[pred])

    time.sleep(8)
