# water-quality

# Smart Community Health Monitoring & Early Warning System
### Water-Borne Disease Risk Detection (Prototype)

This repository contains a **working prototype** for monitoring water quality and predicting **possible water-borne disease risk** in rural areas using **ESP32 + Web Dashboard + Machine Learning**.

The system works **fully offline**, making it suitable for **rural and remote deployment scenarios**.

---

## 🔧 What This Prototype Does

- Simulates a **village-level water monitoring node**
- Monitors:
  - pH
  - TDS
  - Turbidity
  - Water Temperature
- Displays live data on a **web dashboard**
- Uses a **Random Forest ML model** to classify water as:
  - Safe
  - Moderate Risk
  - High Risk
- Supports **multi-device access**:
  - Public view (read-only)
  - Admin control (password protected)

---

## 📁 Folder Structure
smart-water-health-monitor/
│
├── esp32/
│ └── esp32_water_node.ino
│
├── python/
│ ├── train_model.py
│ ├── run_prediction.py
│ ├── evaluate_model.py
│ ├── water_quality_dataset.csv
│ └── model.pkl
│
├── dashboard/
│ ├── public.html
│ └── admin.html
│
└── README.md

---

## 🔌 Hardware Used

- ESP32 WROOM 32
- pH Sensor
- TDS Sensor
- Turbidity Sensor
- DS18B20 Temperature Sensor
- Breadboard & jumper wires

### ESP32 Pin Connections

| Sensor | ESP32 Pin |
|------|----------|
| pH Sensor | GPIO 34 |
| TDS Sensor | GPIO 35 |
| Turbidity Sensor | GPIO 32 |
| DS18B20 | GPIO 4 |
| VCC | 3.3V / 5V |
| GND | GND |

---

## 📡 ESP32 Wi-Fi Details
SSID : Rural-Water-Node
Password : health123


ESP32 acts as a **local offline hotspot** and data source.

---

## 🌐 Dashboards

### Public Dashboard (Teacher / Observer)
- File: `dashboard/public.html`
- Read-only
- Shows live sensor values and water safety status

### Admin Dashboard (Team Control)
- File: `dashboard/admin.html`
- Password: `12345`
- Allows changing:
  - Water condition (Safe / Moderate / Unsafe)
  - Temperature mode

> Changes apply instantly to all connected devices.

---

## 🤖 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Max depth: **10**
- Trained using a **realistic, ESP32-aligned dataset**
- Labels:
  - `0` → Safe
  - `1` → Moderate Risk
  - `2` → High Risk

---

## ▶️ How to Run (IMPORTANT)

### Step 1 — Upload ESP32 Code (Once)
1. Open Arduino IDE
2. Load `esp32/esp32_water_node.ino`
3. Board: **ESP32 Dev Module**
4. Select correct COM port
5. Upload

---

### Step 2 — Power ESP32
- Power using USB from laptop
- Sensors should be connected and powered

---

### Step 3 — Connect to ESP32 Wi-Fi
On **all devices** (laptop / mobile):

Wi-Fi: Rural-Water-Node
Pass : health123


---

### Step 4 — Open Dashboard
- Teacher / Observer:
dashboard/public.html
- Admin (team member):
dashboard/admin.html


---

### Step 5 — Run ML Prediction (One Laptop)
```bash
cd python
python run_prediction.py
```

Example output:
Prediction: SAFE
Prediction: MODERATE RISK
Prediction: HIGH RISK

Data Flow (Simple)
ESP32 → Web Dashboard
ESP32 → Python ML Script
ML → Water Safety Prediction


All data comes from one source (ESP32).

Notes:

This is a prototype, focused on system workflow and analytics
Uses a calibrated simulation layer, common in early pilots
Designed for offline rural deployment

Tip for Demo:

Keep public.html visible
Do not open admin panel unless required
Let values update naturally
