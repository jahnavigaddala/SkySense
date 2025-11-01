# ☁️ SkySense — Smart 6-Day Weather Forecast App

![Made with Node.js](https://img.shields.io/badge/Made%20with-Node.js-green?logo=node.js)
![Flask Dashboard](https://img.shields.io/badge/Dashboard-Flask-blue?logo=flask)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

✅ **Search by City** — Get instant weather updates anywhere in the world  
📍 **Use My Location** — Automatically detect your current position  
🌡️ **Dynamic Backgrounds** — Temperature-based color transitions  
📊 **Interactive Charts** — Displays temperature and humidity trends  
💨 **Live Weather Data** — Shows current weather, humidity, wind, and more  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/SkySense.git
cd SkySense
```

### 2️⃣ Install backend dependencies
```bash
npm install
```

### 3️⃣ (Optional) For the Flask dashboard
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a .env file in the root directory
```yaml
WEATHER_API_KEY=your_api_key_here
```

⚠️ **Never upload your `.env` file** — it contains your private API key.

---

## 🏃 Run the Server
```bash
node server/server.js
```

Then open your browser and go to:  
👉 [http://localhost:3000](http://localhost:3000)

---

## 🌈 Dynamic Background Colors

| Temperature Range | Background Theme |
|-------------------|------------------|
| ≤ 10°C | ❄️ Cool Blue |
| 11–25°C | 🌿 Fresh Green |
| 26–35°C | 🌤️ Warm Yellow |
| > 35°C | 🔥 Hot Red |

---

## 🧠 Tech Stack

### 🌐 Frontend
- **HTML5** — Structure of the web pages (`templates/index.html`)
- **CSS3** — Styling and responsive layout (`static/css/style.css`)
- **JavaScript (ES6)** — Dynamic behavior and chart rendering (`static/js/main.js`)
- **Chart.js** — Interactive temperature and humidity graphs

### ⚙️ Backend
- **Python (Flask Framework)** — Web server and routing (`app.py`)
- **Requests Library** — Fetches data from OpenWeatherMap API
- **Dotenv** — Manages secret environment variables (`.env`)
- **Custom Utilities:**
  - `utils/weather_api.py` — Handles API calls to OpenWeatherMap
  - `utils/format_data.py` — Formats and processes weather data

### 🧩 API
- **OpenWeatherMap API** — Provides real-time and 6-day weather forecasts

### 🔧 Dev Tools & Configuration
- **Git & GitHub** — Version control and code hosting
- **Virtual Environment (venv)** — Isolated Python environment
- **requirements.txt** — Dependency management 

---

## 💡 Future Enhancements

🌤️ Animated weather icons  
🕶️ Dark/Light mode toggle  
💨 Air Quality Index (AQI) integration  
🌍 Multi-language support  
📱 Mobile-friendly dashboard  

---

## 👩‍💻 Developer Info

**Created by:** Jahnavi Gaddala  
**Project:** *SkySense — See the sky like never before.*

---

