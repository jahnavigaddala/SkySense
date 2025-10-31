# 🌦️ SkySense — Smart 5-Day Weather Forecast Web App

![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue?logo=flask)
![Powered by OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)


## ✨ Features

✅ **Search by City** — Get instant weather updates for any city in the world  
📍 **Use My Location** — Auto-detect your current position for forecasts  
🌡️ **Dynamic Background** — Background color adapts to the temperature  
📊 **Interactive Charts** — Temperature and humidity trends for the next 7 days  
💨 **Live Weather Data** — Displays condition, temperature, humidity, wind speed, and local time  

---

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/SkySense.git
cd SkySense
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create a .env file
Inside the root folder, create a file named .env and add your OpenWeatherMap key:

ini
Copy code
OPENWEATHER_API_KEY=your_api_key_here
DEFAULT_CITY=Delhi,IN
⚠️ Don’t upload this .env file to GitHub — it contains your private API key.

🏃 Run the App
bash
Copy code
python app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000

🎨 Dynamic Styling
Temperature Range	Background Theme
≤ 10°C	❄️ Cool Blue
11–25°C	🌿 Fresh Green
26–35°C	🌤️ Warm Yellow
> 35°C	🔥 Hot Red

🧠 Tech Stack
Frontend: HTML, CSS, Chart.js, JavaScript
Backend: Flask (Python)
API: OpenWeatherMap API
Data Format: JSON
Version Control: Git + GitHub

🚀 Deployment (Optional)
You can easily deploy this app on Render or Railway for free:

Push your project to GitHub.

Go to https://render.com.

Click “New Web Service” → Connect your repo.

Add your environment variable:

ini
Copy code
OPENWEATHER_API_KEY=your_api_key_here
Build Command:

bash
Copy code
pip install -r requirements.txt
Start Command:

bash
Copy code
python app.py
✅ Deploy and your app will be live 🎉

💡 Future Enhancements
🌍 Add air quality index (AQI) data

🌅 Add sunrise/sunset animations

📱 Make mobile version more interactive

🤝 Contributing
Pull requests are welcome!
If you find a bug or have an idea for improvement, feel free to open an issue or submit a PR.

🛡️ License
This project is licensed under the MIT License — free to use and modify.

💙 Made with Passion by Jahnavi Gaddala